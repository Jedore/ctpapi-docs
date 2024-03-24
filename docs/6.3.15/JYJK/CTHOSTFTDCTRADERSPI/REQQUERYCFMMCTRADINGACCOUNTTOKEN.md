<p>请求查询监控中心用户令牌，对应响应OnRspQueryCFMMCTradingAccountToken、OnRtnCFMMCTradingAccountToken。</p>
<span class="anchor" id="ce7be024-8464-468f-8b37-9f3e6eca1c73"></span>
## 1.函数原型
<p>virtual int ReqQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID) = 0;</p>
<span class="anchor" id="b9105fb0-49b2-43af-adf7-a40247d45f22"></span>
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
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="2ec1f7b3-635d-4865-bcb1-9342906bcdcc"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fe1f438c-4e01-47de-9957-3342b946f01b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="97129e85-3419-49b5-b3b5-f901a7ebaeca"></span>
## 5.FAQ
<p>无</p>
