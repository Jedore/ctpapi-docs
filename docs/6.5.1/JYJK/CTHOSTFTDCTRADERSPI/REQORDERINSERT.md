<p>报单录入请求，录入错误时对应响应OnRspOrderInsert、OnErrRtnOrderInsert，正确时对应回报OnRtnOrder、OnRtnTrade。</p>
<p>可以录入限价单、市价单、条件单等交易所支持的指令，撤单时使用ReqOrderAction。</p>
<p>不支持预埋单录入，预埋单请使用ReqParkedOrderInsert。</p>
<span class="anchor" id="f3e3a7c3-9969-4705-ae09-22f830d75b05"></span>
## 1.函数原型
<p>virtual int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) = 0;</p>
<span class="anchor" id="6d5eeea4-f0c8-41cf-918d-b34a1d428df7"></span>
## 2.参数
<p>pInputOrder：输入报单</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">值</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">OrderRef</td>
<td style="TEXT-ALIGN: left;">报单引用</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">可自定义或不填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCombOffsetFlagType</td>
<td style="TEXT-ALIGN: left;">CombOffsetFlag</td>
<td style="TEXT-ALIGN: left;">开平标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCombHedgeFlagType</td>
<td style="TEXT-ALIGN: left;">CombHedgeFlag</td>
<td style="TEXT-ALIGN: left;">投机套保标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcDateType</td>
<td style="TEXT-ALIGN: left;">GTDDate</td>
<td style="TEXT-ALIGN: left;">GTD日期</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBusinessUnitType</td>
<td style="TEXT-ALIGN: left;">BusinessUnit</td>
<td style="TEXT-ALIGN: left;">业务单元</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcAccountIDType</td>
<td style="TEXT-ALIGN: left;">AccountID</td>
<td style="TEXT-ALIGN: left;">投资者帐号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">CurrencyID</td>
<td style="TEXT-ALIGN: left;">币种代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcClientIDType</td>
<td style="TEXT-ALIGN: left;">ClientID</td>
<td style="TEXT-ALIGN: left;">客户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcIPAddressType</td>
<td style="TEXT-ALIGN: left;">IPAddress</td>
<td style="TEXT-ALIGN: left;">IP地址</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcMacAddressType</td>
<td style="TEXT-ALIGN: left;">MacAddress</td>
<td style="TEXT-ALIGN: left;">Mac地址</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">VolumeTotalOriginal</td>
<td style="TEXT-ALIGN: left;">数量</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">MinVolume</td>
<td style="TEXT-ALIGN: left;">最小成交量</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBoolType</td>
<td style="TEXT-ALIGN: left;">IsAutoSuspend</td>
<td style="TEXT-ALIGN: left;">自动挂起标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcRequestIDType</td>
<td style="TEXT-ALIGN: left;">RequestID</td>
<td style="TEXT-ALIGN: left;">请求编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBoolType</td>
<td style="TEXT-ALIGN: left;">UserForceClose</td>
<td style="TEXT-ALIGN: left;">用户强评标志</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBoolType</td>
<td style="TEXT-ALIGN: left;">IsSwapOrder</td>
<td style="TEXT-ALIGN: left;">互换单标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderPriceTypeType</td>
<td style="TEXT-ALIGN: left;">OrderPriceType</td>
<td style="TEXT-ALIGN: left;">报单价格条件</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcDirectionType</td>
<td style="TEXT-ALIGN: left;">Direction</td>
<td style="TEXT-ALIGN: left;">买卖方向</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTimeConditionType</td>
<td style="TEXT-ALIGN: left;">TimeCondition</td>
<td style="TEXT-ALIGN: left;">有效期类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeConditionType</td>
<td style="TEXT-ALIGN: left;">VolumeCondition</td>
<td style="TEXT-ALIGN: left;">成交量类型</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcContingentConditionType</td>
<td style="TEXT-ALIGN: left;">ContingentCondition</td>
<td style="TEXT-ALIGN: left;">触发条件</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcForceCloseReasonType</td>
<td style="TEXT-ALIGN: left;">ForceCloseReason</td>
<td style="TEXT-ALIGN: left;">强平原因</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">LimitPrice</td>
<td style="TEXT-ALIGN: left;">价格</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">StopPrice</td>
<td style="TEXT-ALIGN: left;">止损价</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldIPAddressType</td>
<td style="TEXT-ALIGN: left;">reserve2</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p>OrderPriceType：确定输入的报单类型，比如限价单则填写<code>THOST_FTDC_OPT_LimitPrice</code>、市价单则填写<code>THOST_FTDC_OPT_AnyPrice</code>。</p>
<p>Direction：确定买卖方向</p>
<p>CombOffsetFlag：确定开平标志。注:上期所、能源交易所有平今指令，下平仓指令和平昨指令相同</p>
<p>CombHedgeFlag：确定投机套保标志 例:投机 <code>THOST_FTDC_BHF_Speculation</code></p>
<p>TimeCondition：确定报单有效期类型 例:立即完成，否则撤销 <code>THOST_FTDC_TC_IOC</code></p>
<p>VolumeCondition：确定成交量类型</p>
<p>ContingentCondition：确定触发条件</p>
<p>StopPrice：止损价，用于条件单的触发价格</p>
<p>ForceCloseReason：普通用户下单填写<code>THOST_FTDC_FCC_NotForceClose</code> 非强平</p>
<p>IsSwapOrder：互换单填1</p>
<p>CurrencyID：不填写默认为CNY</p>
<p>OrderRef：OrderRef是本地会话全局唯一编号，必须保持递增；可由用户维护，也可由系统自动填写。一定为数字。</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>MacAddress：手工填写本机Mac地址，不自动获取。</p>
<p>BusinessUnit：保留字段。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="354df34e-a9dd-4774-9a09-af69a3edfe83"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2fa5010f-8615-4dcf-ad42-ba75215b61a1"></span>
## 4.调用示例
<pre><code>//限价单:
CThostFtdcInputOrderField ord = { 0 };
strcpy_s(ord.BrokerID, “0000”);
strcpy_s(ord.InvestorID, “00001”); 
strcpy_s(ord.ExchangeID, “SHFE”);
strcpy_s(ord.InstrumentID, “ag1801”);
strcpy_s(ord.UserID, “00001”);
ord.OrderPriceType = THOST_FTDC_OPT_LimitPrice;//限价
ord.Direction = THOST_FTDC_D_Buy;//买
ord.CombOffsetFlag[0] = THOST_FTDC_OF_Open;//开
ord.CombHedgeFlag[0] = THOST_FTDC_HF_Speculation;//投机
ord.LimitPrice = 100;
ord.VolumeTotalOriginal = 1;
ord.TimeCondition = THOST_FTDC_TC_GFD;///当日有效
ord.VolumeCondition = THOST_FTDC_VC_AV;///任意数量
ord.MinVolume = 1;
ord.ContingentCondition = THOST_FTDC_CC_Immediately;
ord.StopPrice = 0;
ord.ForceCloseReason = THOST_FTDC_FCC_NotForceClose;
ord.IsAutoSuspend = 0;
m_pUserApi-&gt;ReqOrderInsert(&amp;ord, nRequestID++);
</code></pre>
<span class="anchor" id="4b705a2f-50dc-4e63-9bc3-5a23e6f707a4"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">郑商所白糖期权的跨式和宽跨式套利指令，在ctp里如何实现？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>和普通的限价单类似，不同的地方是在填写InstrumentID的时候</p>
<p>郑商所跨式组合（STD）: STD SR703C5300&amp;SR703P5300</p>
<p>郑商所宽跨式组合（STG): STG SR703C5300&amp;SR703P5200</p>
<p>支持FAK和FOK</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“已撤单报单被拒绝CZCE:出错:不支持无限制期权组合订单”是什么原因？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>郑商所的组合合约下单，TimeCondition应该用<code>THOST_FTDC_TC_IOC</code>（1）。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如果下单后遇到报错“ctp：每秒报单数超过许可数”，是什么原因？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>这是由于报单频率太快被前置流控所致。投资者可询问期货公司具体的流控设置；期货公司可以自行查看FLEX"程序化交易频繁报撤单管理"中的设置，以及Front的流控配置。注意：Front的流控会放到下一秒，不会报错；FLEX"程序化交易频繁报撤单管理"中的流控会报错。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:报单错误：不允许重复报单”，是什么原因？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>这是表示OrderRef没有递增。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_5" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:无此权限”，是什么原因？</p><div class="region_panel" id="region_panel_5" style="display:block;"><table><tr><td>
<p>这可能InvestorID填写错误，或者该InvestorID不属于UserID的组织架构下。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_5" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_6" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:交易所未处理请求超过许可数”，是什么原因？</p><div class="region_panel" id="region_panel_6" style="display:block;"><table><tr><td>
<p>表示报单频率过快，超过了交易所的流控。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_6" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_7" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:交易所每秒发送请求数超过许可数”，是什么原因？</p><div class="region_panel" id="region_panel_7" style="display:block;"><table><tr><td>
<p>表示报单频率过快，超过了交易所的流控。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_7" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
