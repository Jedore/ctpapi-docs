<p>请求投资者SPBM套餐选择查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINVESTORPORTFDEF/">ReqQrySPBMInvestorPortfDef</a>后，该方法被调用。</p>
<span class="anchor" id="bf7e13da-39e3-4eb3-9600-9b365c996d7f"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInvestorPortfDef(CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="3b30c072-c1bb-457d-b59d-633566afcaf4"></span>
## 2.参数
<p>pSPBMInvestorPortfDef：投资者套餐选择</p>
<pre><code>struct CThostFtdcSPBMInvestorPortfDefField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///组合保证金套餐代码
    TThostFtdcPortfolioDefIDType    PortfolioDefID;
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
<span class="anchor" id="3421a2fa-77fd-4dc6-8517-32dd181e2383"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5603b153-ce3e-4f6a-8ede-e566e55de462"></span>
## 4.FAQ
<p>无</p>
