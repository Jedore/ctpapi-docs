<p>报价录入请求，如果出错，则返回响应OnRspQuoteInsert和OnErrRtnQuoteInsert；正确则推送OnRtnQuote、OnRtnOrder和OnRtnTrade。</p>
<p>单边报价和双边报价，都是用一个接口 ReqQuoteInsert。</p>
<blockquote>
<p>在<code>单边报价</code>的时候，只需要另一边的数量填0，交易核心就能区分开。另外，无论是单边还是双边，Ask/BidOrderRef都是要填的。</p>
</blockquote>
<span class="anchor" id="fb4238b9-1219-493d-8420-8c417cb6ad4f"></span>
## 1.函数原型
<p>virtual int ReqQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, int nRequestID) = 0;</p>
<span class="anchor" id="faf7d3f8-630e-4315-b307-ff0f465f56b0"></span>
## 2.参数
<p>pInputQuote：输入的报价</p>
<pre><code>struct CThostFtdcInputQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///报价引用
    TThostFtdcOrderRefType QuoteRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///卖价格
    TThostFtdcPriceType AskPrice;
    ///买价格
    TThostFtdcPriceType BidPrice;
    ///卖数量
    TThostFtdcVolumeType AskVolume;
    ///买数量
    TThostFtdcVolumeType BidVolume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///卖开平标志
    TThostFtdcOffsetFlagType AskOffsetFlag;
    ///买开平标志
    TThostFtdcOffsetFlagType BidOffsetFlag;
    ///卖投机套保标志
    TThostFtdcHedgeFlagType AskHedgeFlag;
    ///买投机套保标志
    TThostFtdcHedgeFlagType BidHedgeFlag;
    ///衍生卖报单引用
    TThostFtdcOrderRefType AskOrderRef;
    ///衍生买报单引用
    TThostFtdcOrderRefType BidOrderRef;
    ///应价编号
    TThostFtdcOrderSysIDType ForQuoteSysID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>ForQuoteSysID：询价编号，用于唯一定位一笔询价</p>
<p>BidOrderRef：要比AskOrderRef大。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="91571194-c7dd-4254-b0c8-d7a38de15ff8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4729c91c-d87b-4816-836a-6cea42adc103"></span>
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
<span class="anchor" id="6280aae0-c09a-485e-8bff-dc647f9a9560"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">询价时报：“没有该合约的做市商”？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>这是因为询价合约不对，目前期权合约可以参加询价。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">询价时报：“CTP：当前时间禁止询价”？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>这是因为期货公司一般把询价限制时间设置为60秒询价一次，周期内不能多次询价。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">询价时报：“CTP：当前价差禁止询价”？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
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
<p><div class="region_i" id=""><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“非法的做市商响应”是什么原因？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>这可能是所用交易编码非做市商专用所致。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_5" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">各家交易所第二次报价是否会撤销第一次报价？</p><div class="region_panel" id="region_panel_5" style="display:block;"><table><tr><td>
<p>中金所：不会撤销</p>
<p>大商所：不会撤销</p>
<p>郑商所：会撤销</p>
<p>上期所：会撤销</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_5" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
