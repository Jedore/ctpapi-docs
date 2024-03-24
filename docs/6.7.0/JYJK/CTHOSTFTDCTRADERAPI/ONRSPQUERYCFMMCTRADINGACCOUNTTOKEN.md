<p>请求查询监控中心用户令牌，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYCFMMCTRADINGACCOUNTTOKEN/">ReqQueryCFMMCTradingAccountToken</a>后，该方法被调用。</p>
<span class="anchor" id="28a76c5e-e3df-4e4e-b254-6d69cb8ffa74"></span>
## 1.函数原型
<p>virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4e4264b7-9713-4c64-af50-90b809bd6dd5"></span>
## 2.参数
<p>pQueryCFMMCTradingAccountToken：查询监控中心用户令牌</p>
<pre><code>struct CThostFtdcQueryCFMMCTradingAccountTokenField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="e68ea44d-61aa-45ef-af16-7534eaea17d3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9bf35133-12cc-48ba-bb0d-ba066eb6ac48"></span>
## 4.FAQ
<p>无</p>
