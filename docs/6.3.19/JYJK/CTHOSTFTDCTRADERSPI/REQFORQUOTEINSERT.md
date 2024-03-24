<p>询价录入请求</p>
<p>错误响应: OnErrRtnForQuoteInsert，OnRspForQuoteInsert</p>
<p>正确响应: OnRtnForQuoteRsp</p>
<span class="anchor" id="c5001619-e3c3-4147-bfd9-6ceae0a7611e"></span>
## 1.函数原型
<p>virtual int ReqForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID) = 0;</p>
<span class="anchor" id="6e7dfefc-1b0d-494c-bb2b-4c39b521eb17"></span>
## 2.参数
<p>pInputForQuote：输入的询价</p>
<pre><code>struct CThostFtdcInputForQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///询价引用
    TThostFtdcOrderRefType ForQuoteRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="f3b69d58-3088-4239-b240-d19307b07ffc"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3274938a-8335-49db-a881-4fa63d0e39d7"></span>
## 4.调用示例
<pre><code>CThostFtdcInputForQuoteField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.UserID, "1000001");
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqForQuoteInsert(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="a36fb483-eb60-478d-b634-5b80e6a2bcc7"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">询价时报：“没有该合约的做市商”？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>询价合约不对。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
