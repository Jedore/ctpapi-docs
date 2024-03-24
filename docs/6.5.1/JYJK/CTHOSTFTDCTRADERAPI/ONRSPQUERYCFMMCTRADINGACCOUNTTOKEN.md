<p>请求查询监控中心用户令牌，当执行ReqQueryCFMMCTradingAccountToken后，该方法被调用。</p>
<span class="anchor" id="b1ec36af-15ca-4765-8b04-0f58e967b312"></span>
## 1.函数原型
<p>virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7a6e457b-2a70-4f02-ab57-074ea501fa35"></span>
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
<span class="anchor" id="75dd5fbd-900c-4581-a6c7-3a49bf640d90"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="325e65c0-02c5-4db5-8479-fb5a5752b9fd"></span>
## 4.FAQ
<p>无</p>
