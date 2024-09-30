<p>请求投资者SPBM套餐选择查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINVESTORPORTFDEF/">ReqQrySPBMInvestorPortfDef</a>后，该方法被调用。</p>
<span class="anchor" id="285c9f6f-c781-4258-aed7-1fb31300a543"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInvestorPortfDef(CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1cfb7057-5acb-4a73-a592-5c3d451647a5"></span>
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
<span class="anchor" id="4fec1719-f021-47fe-9cfd-3bf6d0afc7d9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="97c72d9e-0e56-4afb-9b75-432ad49143c3"></span>
## 4.FAQ
<p>无</p>
