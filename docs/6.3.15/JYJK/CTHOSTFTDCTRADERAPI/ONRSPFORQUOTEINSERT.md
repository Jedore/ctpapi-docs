<p>询价录入请求响应，当执行ReqForQuoteInsert后有字段填写不对之类的CTP报错则通过此接口返回。</p>
<span class="anchor" id="375dc10a-ac02-4a44-9f7e-fd91e2ed5c85"></span>
## 1.函数原型
<p>virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a88db45d-daf7-4bcb-a269-0be7b429dcba"></span>
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
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="b680e389-64a8-4d26-8ae1-c4bdab20dd73"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="90c487b3-69b7-435b-b8a9-5b30c646a7fc"></span>
## 4.FAQ
<p>无</p>
