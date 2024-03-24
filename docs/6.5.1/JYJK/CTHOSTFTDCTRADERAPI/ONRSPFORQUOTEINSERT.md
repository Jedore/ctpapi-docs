<p>询价录入请求响应，当执行ReqForQuoteInsert后有字段填写不对之类的CTP报错则通过此接口返回。</p>
<span class="anchor" id="b7c8f879-c7ad-4c4f-a031-40fb1fb482f7"></span>
## 1.函数原型
<p>virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1744aa85-4dda-4b6f-aa4c-ada3d6a95830"></span>
## 2.参数
<p>pInputForQuote：输入的询价</p>
<pre><code>struct CThostFtdcInputForQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///询价引用
    TThostFtdcOrderRefType  ForQuoteRef;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
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
<span class="anchor" id="fd2505c4-a331-469e-9610-b7ff8d502bb0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fe677fc0-1f0a-4c6d-81f2-3cfee183c5c0"></span>
## 4.FAQ
<p>无</p>
