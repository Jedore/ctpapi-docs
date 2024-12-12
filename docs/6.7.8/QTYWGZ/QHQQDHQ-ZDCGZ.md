<p>本文旨在说明行权和自对冲在CTP上的实现，具体业务规则以交易所为准。</p>
<span class="anchor" id="d23ed505-9915-45eb-9be0-896d7429a298"></span>
## 1. 接口说明
<ul>
<li>行权申请指令</li>
</ul>
<p>行权申请：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERINSERT/">ReqExecOrderInsert</a></p>
<p>错误响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNEXECORDERINSERT/">OnErrRtnExecOrderInsert</a>，<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPEXECORDERINSERT/">OnRspExecOrderInsert</a></p>
<p>正确响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNEXECORDER/">OnRtnExecOrder</a></p>
<ul>
<li>行权撤销指令</li>
</ul>
<p>行权撤销：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERACTION/">ReqExecOrderAction</a></p>
<p>错误响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNEXECORDERACTION/">OnErrRtnExecOrderAction</a>，<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPEXECORDERACTION/">OnRspExecOrderAction</a></p>
<p>正确响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNEXECORDER/">OnRtnExecOrder</a></p>
<ul>
<li>期权自对冲指令</li>
</ul>
<p>自对冲申请：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a></p>
<p>错误响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNOPTIONSELFCLOSEINSERT/">OnErrRtnOptionSelfCloseInsert</a>，<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPOPTIONSELFCLOSEINSERT/">OnRspOptionSelfCloseInsert</a></p>
<p>正确响应：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a></p>
<ul>
<li>期权自对冲撤销指令</li>
</ul>
<p>自对冲撤销：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEACTION/">ReqOptionSelfCloseAction</a></p>
<p>错误响应: <a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNOPTIONSELFCLOSEACTION/">OnErrRtnOptionSelfCloseAction</a>，<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPOPTIONSELFCLOSEACTION/">OnRspOptionSelfCloseAction</a></p>
<p>正确响应: <a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNOPTIONSELFCLOSE/">OnRtnOptionSelfClose</a></p>
<span class="anchor" id="6f52cc57-6c70-4e09-815e-8ff79179c555"></span>
## 2. 行权执行指令
<span class="anchor" id="a07a5701-5898-4ed7-8def-897b8a275e4f"></span>
### 2.1. 申请指令
<p>行权指令包括<strong>申请行权</strong>和<strong>放弃行权</strong>。</p>
<p>美式期权的买方在合约到期日及其之前任一交易日均可行使权利，可以在到期日之前任一交易日的交易时间，以及到期日15:30之前提出行权申请；欧式期权的买方只可在合约到期日当天行使权利，到期日同最后交易日。欧式和美式如下表所示：</p>
<table><tr><th style="TEXT-ALIGN: center;">　</th><th style="TEXT-ALIGN: center;">CFFEX</th><th style="TEXT-ALIGN: center;">CZCE</th><th style="TEXT-ALIGN: center;">DCE</th><th style="TEXT-ALIGN: center;">INE</th><th style="TEXT-ALIGN: center;">SHFE</th></tr><tr><td style="TEXT-ALIGN: center;">美式</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">白糖期权<br/>棉花期权<br/>PTA期权<br/>甲醇期权<br/>菜籽粕期权<br/></td>
<td style="TEXT-ALIGN: center;">豆粕期权<br/>玉米期权<br/>铁矿石期权<br/>液化石油气期权</td>
<td style="TEXT-ALIGN: center;">原油期权</td>
<td style="TEXT-ALIGN: center;">橡胶期权<br/>铝期权<br/>锌期权</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">欧式</td>
<td style="TEXT-ALIGN: center;">沪深300股指期权</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">铜期权<br/>黄金期权</td>
</tr>
</table>
<p>如果非到期日申请，<strong>CTP不做判断</strong>，报入交易所后会返回报错：报单被拒绝，不在宣告期内。</p>
<p>行权会锁仓，并冻结资金。可行权的仓位根据多头持仓减去冻结持仓，同时计算可用资金满足支付行权权利金的仓位，二者取最小值作为可行权的实际仓位。行权冻结的仓体现在StrikeFrozen字段。</p>
<p>放弃行权会锁仓，但是不冻结资金。放弃行权冻结的仓体现在AbandonFrozen字段。</p>
<p>目前行权和放弃行权都使用<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERINSERT/">ReqExecOrderInsert</a>接口，通过ActionType区分：行权申请THOST_FTDC_ACTP_Exec，放弃行权申请THOST_FTDC_ACTP_Abandon。</p>
<blockquote>
<p>中金所目前不支持现货期权的相关行权指令，支持期货期权的行权指令。</p>
<p>针对上期所开平标志可以报入平今THOST_FTDC_OF_CloseToday，平昨THOST_FTDC_OF_CloseYesterday和平仓THOST_FTDC_OF_Close。其中平仓的逻辑跟平仓单的逻辑一样，如果客户报入平仓单，实际上CTP会处理为平昨仓。</p>
</blockquote>
<span class="anchor" id="1fbbe2a9-7a0e-4491-b6df-83ee12482ad3"></span>
### 2.2. 自动行权、放弃行权和取消到期日自动行权
<p>交易所会在期权合约到期日闭市后，默认自动将客户的实值期权进行行权，虚值期权放弃行权。如果客户不想执行某个实值期权，可在最后交易日申请放弃行权。</p>
<ul>
<li><p>上期、能源、郑州支持放弃行权。</p></li>
<li><p>中金所对于现货期权不支持通过柜台系统（例如CTP）放弃行权，只支持通过会服系统进行操作。</p></li>
<li><p>大商所不支持放弃行权，只支持取消到期日自动行权。例如，投资者10手实值期权，若要放弃其中2手，则需要先取消到期日自动行权，然后再申报行权8手，以此达到目的。</p></li>
</ul>
<blockquote>
<p>大商所取消到期日自动行权方法为：使用接口<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERINSERT/">ReqExecOrderInsert</a>，行权数量<strong>Volume填0</strong>。对数量不做校验，不冻钱不冻仓，只有到期日才能报入。</p>
</blockquote>
<p>通过接口<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQQRYEXECORDER/">ReqQryExecOrder</a>可以查询已报入交易系统的申请指令。</p>
<p><span alt="" id="anchor-id-02"></span> </p>
<span class="anchor" id="ad296074-2406-4ca0-a79f-92dbd7f8a309"></span>
### 2.3. 撤销申请指令
<p>对于已报入交易系统的行权申请或放弃申请指令，CTP提供接口<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERACTION/">ReqExecOrderAction</a>撤销申请。</p>
<p>指令通过<strong>ActionType</strong>字段取值<strong>THOST_FTDC_ACTP_Exec</strong>、</p>
<p><strong>FrontID</strong>、<strong>SessionID</strong>、<strong>ExecOrderRef</strong>、<strong>InstrumentID</strong>四个字段为一组条件撤销一笔申请（6.7.2开始支持撤销其他席位发起的“取消到期自动行权”指令或“期权自对冲”指令，由于接收其他席位的指令frontid+sessionid都是0，填0即可）。</p>
<span class="anchor" id="718e3e2d-3f31-43a1-8879-26bffca48c1c"></span>
## 3. 自对冲
<p>自对冲的业务含义是指向交易所提出申请将同一期权的多空头仓位，或者期权行权后或者履约后形成的期货的多空头仓位自我对冲掉。</p>
<blockquote>
<p>目前郑商所和中金所的自对冲业务都是走会服系统，不通过交易通道。本栏目内容不包含郑商所和中金所</p>
</blockquote>
<span class="anchor" id="90e7b4ba-4f1a-40ec-8816-f9ed1c59ffaa"></span>
### 3.1. 行权后期货自对冲
<p>期权买方（卖方）可以申请对其同一交易编码下行权后（履约后）双向期货持仓进行对冲平仓，对冲数量不超过行权获得的期货持仓量。对冲结果从当日期货持仓量中扣除，并计入成交量。</p>
<p>多头持仓的行权后期货自对冲仍采用行权接口<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERINSERT/">ReqExecOrderInsert</a>，其中<strong>CloseFlag</strong>取值<strong>THOST_FTDC_EOCF_AutoClose</strong>来实现。</p>
<p>针对空头持仓的履约后期货自对冲提供接口<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>，通过<strong>OptSelfCloseFlag</strong>字段取值<strong>THOST_FTDC_OSCF_SellCloseSelfFuturePosition</strong>实现。</p>
<span class="anchor" id="73d4bd1b-0192-4aab-bbc8-881ab3b6d072"></span>
### 3.2. 期权自对冲
<p>客户可以申请对其同一交易编码下的双向期权持仓进行对冲平仓。对冲结果从当日期权持仓量中扣除，并计入成交量。</p>
<p>期权自对冲通过<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>接口，<strong>OptSelfCloseFlag</strong>字段取值<strong>THOST_FTDC_OSCF_CloseSelfOptionPosition</strong>申报。</p>
<p>该指令支持指定数量申请<strong>Volume</strong>，但是对仓位和资金都不做校验，比如某个投资者对期权合约并没有仓位，但是也可以申请期权自对冲。交易所盘后会去校验。投资者可以修改手数，目前CTP提供接口<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEACTION/">ReqOptionSelfCloseAction</a>，支持撤销自对冲后，重新申请。</p>
<p>上期所期权自对冲仅普通投资者可申请。针对同一客户，同合约和同开平标志(OffsetFlag)，只维护一条信息，后续报入的指令，都是更新操作。既期权自对冲本地报单编号相同。比如同一投资者对某一个铜期权申请期权自对冲3手，然后再报入该指令，申请期权自对冲5手，那么交易所查询的期权自对冲记录依然是一条，但是手数变为5。</p>
<p>大商所的期权自对冲普通投资者和做市商都可以申请，该设置是指定合约，不区分投机和套保，不指定数量，当日有效。</p>
<span class="anchor" id="08c10030-9e9f-409e-bc75-f85fa4779ed0"></span>
### 3.3. 做市商留仓
<p>交易所默认每天对做市商的期权买卖仓位自对冲（平仓），所以提供该选项给做市商，可以去申请留仓，当天不要被自对冲。</p>
<p>沿用<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>接口，<strong>OptSelfCloseFlag</strong>字段取值<strong>THOST_FTDC_OSCF_CloseSelfOptionPosition</strong>申报。</p>
<blockquote>
<p>目前仅支持上期所做市商留仓申请</p>
</blockquote>
