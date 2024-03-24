<p>请求查询监控中心用户令牌，当执行ReqQueryCFMMCTradingAccountToken后，该方法被调用。</p>
<span class="anchor" id="8fa4d57b-9836-4060-82fc-617b25492d42"></span>
## 1.函数原型
<p>virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="bea96950-d7ab-4e15-9453-e1861dc93484"></span>
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
<span class="anchor" id="7f60c0c6-727f-4ec3-9c72-d91dd1875d82"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8b355f98-59ee-43bb-890e-c2c3844500e0"></span>
## 4.FAQ
<p>无</p>
