<p>请求投资者SPBM套餐选择查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINVESTORPORTFDEF/">ReqQrySPBMInvestorPortfDef</a>后，该方法被调用。</p>
<span class="anchor" id="74ac3c43-6b99-4602-af1c-4ca31e40922b"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInvestorPortfDef(CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1f3237fa-8b62-4a40-bb2a-603b81e48906"></span>
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
<span class="anchor" id="d49c6cd9-6557-4391-942b-57ada8c2a944"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4b98874e-4930-41b8-9274-f6483496db25"></span>
## 4.FAQ
<p>无</p>
