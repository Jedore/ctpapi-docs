<p>报单操作请求</p>
<p>错误响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPORDERACTION/">OnRspOrderAction</a>，<a href="../../CTHOSTFTDCTRADERAPI/ONERRRTNORDERACTION/">OnErrRtnOrderAction</a></p>
<p>正确响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a></p>
<span class="anchor" id="6c7d0c01-c26c-45f5-800e-614c78ddca50"></span>
## 1.函数原型
<p>virtual int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="08d25f54-b499-4c07-bc9a-5d4baaeeebd7"></span>
## 2.参数
<p>pInputOrderAction：输入报单操作</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">OrderRef</td>
<td style="TEXT-ALIGN: left;">报单引用</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderSysIDType</td>
<td style="TEXT-ALIGN: left;">OrderSysID</td>
<td style="TEXT-ALIGN: left;">报单编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*2</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderActionRefType</td>
<td style="TEXT-ALIGN: left;">OrderActionRef</td>
<td style="TEXT-ALIGN: left;">报单操作引用</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填，递增</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcRequestIDType</td>
<td style="TEXT-ALIGN: left;">RequestID</td>
<td style="TEXT-ALIGN: left;">请求编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcFrontIDType</td>
<td style="TEXT-ALIGN: left;">FrontID</td>
<td style="TEXT-ALIGN: left;">前置编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSessionIDType</td>
<td style="TEXT-ALIGN: left;">SessionID</td>
<td style="TEXT-ALIGN: left;">会话编号</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填*1</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">VolumeChange</td>
<td style="TEXT-ALIGN: left;">数量变化</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcActionFlagType</td>
<td style="TEXT-ALIGN: left;">ActionFlag</td>
<td style="TEXT-ALIGN: left;">操作标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">LimitPrice</td>
<td style="TEXT-ALIGN: left;">价格</td>
<td style="TEXT-ALIGN: left;">无</td>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldIPAddressType</td>
<td style="TEXT-ALIGN: left;">reserve2</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderMemoType</td>
<td style="TEXT-ALIGN: left;">OrderMemo</td>
<td style="TEXT-ALIGN: left;">报单回显字段</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSequenceNo12Type</td>
<td style="TEXT-ALIGN: left;">SessionReqSeq</td>
<td style="TEXT-ALIGN: left;">session上请求计数 api自动维护</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
</table>
<p><strong><font color="#FF0000">必填*1、必填*2</font></strong>：两组选一组必填，能对应要撤的报单。</p>
<p>OrderRef：对应要撤销的那笔报单的报单引用</p>
<p>FrontID: 对应要撤销的那笔报单的前置编号</p>
<p>SessionID: 对应要撤销的那笔报单的会话编号</p>
<p>ExchangeID: 对应要撤销的那笔报单的交易所ID</p>
<p>OrderSysID: 对应要撤销的那笔报单的报单编号</p>
<p>ActionFlag：只支持删除，不支持修改、激活、挂起。对于由其他柜台做的激活或挂起的报单，ctp系统能正常接收。</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>OrderMemo:报单回显字段，OrderMemo字段可供终端厂商标记订单使用，CTP不做处理，即终端填写什么CTP就返回什么</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="9fd8135f-dc29-4489-aa13-5caf6e36bcaa"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="96a8b759-54c9-42e3-8ed0-0c786fdb2703"></span>
## 4.调用示例
<p>//第一种方法，使用OrderSysID撤单（<strong><font style="color:red">推荐使用</font></strong>）</p>
<pre><code>CThostFtdcInputOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.OrderSysID, "         131");  //对应要撤报单的OrderSysID
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.InstrumentID, "rb1809");
ActionFlag = THOST_FTDC_AF_Delete;
m_pUserApi-&gt;ReqOrderAction(&amp;a, nRequestID++);
</code></pre>
<p>//第二种方法，使用FrontID+SessionID+OrderRef撤单</p>
<pre><code>CThostFtdcInputOrderActionField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.UserID, "1000001");
a.FrontID = 1;   //对应要撤报单的FrontID
a.SessionID = -788541;   //对应要撤报单的sessionid
strcpy_s(a.OrderRef, "        3");   //对应要撤报单的OrderRef
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.InstrumentID, "rb1809");
ActionFlag = THOST_FTDC_AF_Delete;
m_pUserApi-&gt;ReqOrderAction(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="05d4c823-5470-4044-97d6-b090e6b141f2"></span>
## 5.FAQ
<p><span alt="" id="anchor-id-01"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">ctp支持撤销未知单吗？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>目前665版本以上柜台不允许撤郑商所的未知单，其他交易所都是可以撤未知单的。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
