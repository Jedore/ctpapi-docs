<p>请求查询监控中心用户令牌，当执行ReqQueryCFMMCTradingAccountToken后，该方法被调用。</p>
<span class="anchor" id="1a4ebcfd-62a2-4a3d-82cd-721a26c986a1"></span>
## 1.函数原型
<p>virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="46db7294-162b-4463-bdb5-d7a0582bb6bb"></span>
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
<span class="anchor" id="b57377dc-253e-4440-b23d-c60fb2f0c8c0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="89f44f25-ad43-4a45-b476-15e1760532e6"></span>
## 4.FAQ
<p>无</p>
