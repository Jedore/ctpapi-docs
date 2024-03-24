<p>询价录入错误回报，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQFORQUOTEINSERT/">ReqForQuoteInsert</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="111d1fac-2b31-4c45-8c4b-287af851a86a"></span>
## 1.函数原型
<p>virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="54069ba2-388f-41f0-814c-a5f1b5a5d7ce"></span>
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
<span class="anchor" id="c80578b9-b261-4d15-be4b-50651c433455"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6af59dc6-cf1b-4e6d-9a0f-ccc73fd7bbfe"></span>
## 4.FAQ
<p>无</p>
