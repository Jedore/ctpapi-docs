<p>询价录入错误回报，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQFORQUOTEINSERT/">ReqForQuoteInsert</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="bf5f3e01-5a3e-41f3-aa36-0db26eb67f26"></span>
## 1.函数原型
<p>virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="d6ca6ae2-1ed0-4ffb-8c18-fd93a02b4682"></span>
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
<span class="anchor" id="0ff1c430-25d1-4029-aa6c-35e8f84fa029"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="04214522-14ed-4f43-bce6-e07ad6d4bc70"></span>
## 4.FAQ
<p>无</p>
