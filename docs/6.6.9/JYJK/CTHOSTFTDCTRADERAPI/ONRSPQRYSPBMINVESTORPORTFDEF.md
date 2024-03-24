<p>请求投资者SPBM套餐选择查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMINVESTORPORTFDEF/">ReqQrySPBMInvestorPortfDef</a>后，该方法被调用。</p>
<span class="anchor" id="3e7237a8-227f-4f6b-a9b0-40c864ccd63c"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMInvestorPortfDef(CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="77c7a03f-b0dc-4756-bbce-d1add97edaf1"></span>
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
<span class="anchor" id="daede3cf-ba54-42b6-aa43-5aea2b8cad30"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2b575c37-de08-4fd4-882c-fe84da2eae33"></span>
## 4.FAQ
<p>无</p>
