<p>请求查询监控中心用户令牌，对应响应OnRspQueryCFMMCTradingAccountToken、OnRtnCFMMCTradingAccountToken。</p>
<span class="anchor" id="e6901d29-6ac9-48e0-985a-57ad01912379"></span>
## 1.函数原型
<p>virtual int ReqQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID) = 0;</p>
<span class="anchor" id="5eadb536-70c5-4a28-8abd-1b000adb0690"></span>
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
<span class="anchor" id="bd07a038-35af-4fc1-9efd-b2ab4f1e46ab"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1a4ed11a-4218-4eee-a283-c2350fb71aef"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4b62f383-abce-48f1-bb22-b1a80710dc90"></span>
## 5.FAQ
<p>无</p>
