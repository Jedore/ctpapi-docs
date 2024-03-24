<p>请求投资者SPBM套餐选择查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINVESTORPORTFDEF/">ReqQrySPBMInvestorPortfDef</a>后，该方法被调用。</p>
<span class="anchor" id="71702c66-0426-4263-9abb-4bcbafd373fe"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInvestorPortfDef(CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6909120a-96ac-457d-b942-cba5f77bd326"></span>
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
<span class="anchor" id="0d5df6c1-13b6-46c9-a535-7fe498b66134"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2cd03ceb-3d79-4f94-a15f-be2b11f52a24"></span>
## 4.FAQ
<p>无</p>
