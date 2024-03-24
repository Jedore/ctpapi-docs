<p>询价录入错误回报，当执行ReqForQuoteInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="fccc7b65-ed26-41c0-a07f-900c55e75522"></span>
## 1.函数原型
<p>virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="a9694b1f-fd6e-44fc-84da-a42330bb0694"></span>
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
<span class="anchor" id="07f2b1c5-bf57-4dbb-b79a-28a7e4a85b2e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c2cd3d27-492c-4d26-8cd6-2c63f1dedb93"></span>
## 4.FAQ
<p>无</p>
