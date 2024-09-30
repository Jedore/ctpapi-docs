<p>报价录入请求，如果出错，则返回响应<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQUOTEINSERT/">OnRspQuoteInsert</a>和<a href="../../CTHOSTFTDCTRADERAPI/ONERRRTNQUOTEINSERT/">OnErrRtnQuoteInsert</a>；正确则推送<a href="../../CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>、<a href="../../CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>和<a href="../../CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>。</p>
<p>单边报价和双边报价，都是用一个接口 ReqQuoteInsert。</p>
<blockquote>
<p>在<code>单边报价</code>的时候，只需要另一边的数量填0，交易核心就能区分开。另外，无论是单边还是双边，Ask/BidOrderRef都是要填的。</p>
<p>除上期所的期货合约使用<a href="../REQORDERINSERT/">ReqOrderInsert</a>接口报价，其他交易所均使用本接口报价。</p>
</blockquote>
<span class="anchor" id="33bee6f5-7866-436e-bd77-df1187ad906f"></span>
## 1.函数原型
<p>virtual int ReqQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, int nRequestID) = 0;</p>
<span class="anchor" id="9dd03139-359d-48c4-a0c0-cc94153a0a7b"></span>
## 2.参数
<p>pInputQuote：输入的报价</p>
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
<td style="TEXT-ALIGN: left;">QuoteRef</td>
<td style="TEXT-ALIGN: left;">报价引用</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcUserIDType</td>
<td style="TEXT-ALIGN: left;">UserID</td>
<td style="TEXT-ALIGN: left;">用户代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBusinessUnitType</td>
<td style="TEXT-ALIGN: left;">BusinessUnit</td>
<td style="TEXT-ALIGN: left;">业务单元</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">AskOrderRef</td>
<td style="TEXT-ALIGN: left;">衍生卖报单引用</td>
<td style="TEXT-ALIGN: left;">选填</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderRefType</td>
<td style="TEXT-ALIGN: left;">BidOrderRef</td>
<td style="TEXT-ALIGN: left;">衍生买报单引用</td>
<td style="TEXT-ALIGN: left;">选填</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderSysIDType</td>
<td style="TEXT-ALIGN: left;">ForQuoteSysID</td>
<td style="TEXT-ALIGN: left;">应价编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestUnitIDType</td>
<td style="TEXT-ALIGN: left;">InvestUnitID</td>
<td style="TEXT-ALIGN: left;">投资单元代码</td>
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
<td style="TEXT-ALIGN: left;">AskVolume</td>
<td style="TEXT-ALIGN: left;">卖数量</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcVolumeType</td>
<td style="TEXT-ALIGN: left;">BidVolume</td>
<td style="TEXT-ALIGN: left;">买数量</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcRequestIDType</td>
<td style="TEXT-ALIGN: left;">RequestID</td>
<td style="TEXT-ALIGN: left;">请求编号</td>
<td style="TEXT-ALIGN: left;">无</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOffsetFlagType</td>
<td style="TEXT-ALIGN: left;">AskOffsetFlag</td>
<td style="TEXT-ALIGN: left;">卖开平标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOffsetFlagType</td>
<td style="TEXT-ALIGN: left;">BidOffsetFlag</td>
<td style="TEXT-ALIGN: left;">买开平标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcHedgeFlagType</td>
<td style="TEXT-ALIGN: left;">AskHedgeFlag</td>
<td style="TEXT-ALIGN: left;">卖投机套保标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">投机</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcHedgeFlagType</td>
<td style="TEXT-ALIGN: left;">BidHedgeFlag</td>
<td style="TEXT-ALIGN: left;">买投机套保标志</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">投机</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">AskPrice</td>
<td style="TEXT-ALIGN: left;">卖价格</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPriceType</td>
<td style="TEXT-ALIGN: left;">BidPrice</td>
<td style="TEXT-ALIGN: left;">买价格</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">必填</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldIPAddressType</td>
<td style="TEXT-ALIGN: left;">reserve2</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOrderSysIDType</td>
<td style="TEXT-ALIGN: left;">ReplaceSysID</td>
<td style="TEXT-ALIGN: left;">被顶单编号</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTimeConditionType</td>
<td style="TEXT-ALIGN: left;">TimeCondition</td>
<td style="TEXT-ALIGN: left;">有效期类型</td>
<td style="TEXT-ALIGN: left;">否</td>
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
<p>ForQuoteSysID：询价编号，用于唯一定位一笔询价，需要纯数字递增</p>
<p>AskOrderRef：需要纯数字递增</p>
<p>BidOrderRef：要比AskOrderRef大，需要纯数字递增</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。填写规则如下：ipv4原样填写，ipv6要转成非零压缩地址，即原始地址，同时要去掉冒号，eg：AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH</p>
<p>OrderMemo:报单回显字段，OrderMemo字段可供终端厂商标记订单使用，CTP不做处理，即终端填写什么CTP就返回什么</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e209bbd0-7bfa-4cdb-aa6a-cb46e80d562a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5fe178ac-d867-4f6d-ae21-9d5b70a9be31"></span>
## 4.示例调用
<pre><code>CThostFtdcInputQuoteField t = { 0 };
strcpy_s(t.BrokerID, "9999");
strcpy_s(t.InvestorID, "1000001");
strcpy_s(t.InstrumentID, "rb1809");
strcpy_s(t.UserID, "1000001"); 
strcpy_s(t.ExchangeID, "SHFE"); 
t.AskPrice = 200;
t.BidPrice = 150;
t.AskVolume = 1;
t.BidVolume = 1;
t.AskOffsetFlag = THOST_FTDC_OF_Open;///卖开平标志
t.BidOffsetFlag = THOST_FTDC_OF_Open;///买开平标志
t.AskHedgeFlag = THOST_FTDC_HF_Hedge;///卖投机套保标志
t.BidHedgeFlag = THOST_FTDC_HF_Hedge;///买投机套保标志
_itoa_s(OrderRef, t.AskOrderRef, 10);///衍生卖报单引用
OrderRef++;
_itoa_s(OrderRef, t.BidOrderRef, 10);///衍生买报单引用
OrderRef++; 
m_pUserApi-&gt;ReqQuoteInsert(&amp;t, nRequestID++);
</code></pre>
<span class="anchor" id="49a54b62-ce51-40d8-9530-3ea519aedee2"></span>
## 5.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">询价时报：“没有该合约的做市商”？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>这是因为询价合约不对，目前期权合约可以参加询价。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">询价时报：“CTP：当前时间禁止询价”？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>这是因为期货公司一般把询价限制时间设置为60秒询价一次，周期内不能多次询价。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">询价时报：“CTP：当前价差禁止询价”？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>交易所有询价价差的限制，期货公司可以在柜台上进行设置，一般如下：</p>
<table><tr><th style="TEXT-ALIGN: center;">经纪公司代码</th><th style="TEXT-ALIGN: center;">合约代码</th><th style="TEXT-ALIGN: center;">交易所代码</th><th style="TEXT-ALIGN: center;">最新价</th><th style="TEXT-ALIGN: center;">价差</th></tr><tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">0</td>
<td style="TEXT-ALIGN: left;">8</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">50</td>
<td style="TEXT-ALIGN: left;">10</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">100</td>
<td style="TEXT-ALIGN: left;">20</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">200</td>
<td style="TEXT-ALIGN: left;">30</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">300</td>
<td style="TEXT-ALIGN: left;">50</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">1008</td>
<td style="TEXT-ALIGN: left;">SRC</td>
<td style="TEXT-ALIGN: left;">CZCE</td>
<td style="TEXT-ALIGN: left;">500</td>
<td style="TEXT-ALIGN: left;">75</td>
</tr>
</table>
<p>询价价差的判断过程</p>
<p>1）看最新价对应于上面的哪一档次，确定价差的最小值</p>
<p>2）计算买价和卖价的价差，看是否大于设置的价差（等于也不行）</p>
<p>如果2）通过，那么询价单报入交易所，否则会被CTP直接拒绝。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“非法的做市商响应”是什么原因？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>这可能是所用交易编码非做市商专用所致。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_5" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">各家交易所第二次报价是否会撤销第一次报价？</p><div class="region_panel" id="region_panel_5" style="display:block;"><table><tr><td>
<p>中金所：不会撤销</p>
<p>大商所：不会撤销</p>
<p>郑商所：会撤销</p>
<p>上期所：会撤销</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_5" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_6" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">各家交易所使用的报价接口是否一样？</p><div class="region_panel" id="region_panel_6" style="display:block;"><table><tr><td>
<p>中金所：只有期权做市商,使用ReqQuoteInsert</p>
<p>大商所：使用ReqQuoteInsert</p>
<p>郑商所：使用ReqQuoteInsert</p>
<p>上期所：期货合约使用<a href="../REQORDERINSERT/">ReqOrderInsert</a>，期权合约使用ReqQuoteInsert</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_6" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
