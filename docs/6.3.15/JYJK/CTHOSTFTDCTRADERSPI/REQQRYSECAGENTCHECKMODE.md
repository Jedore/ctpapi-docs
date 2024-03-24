<p>请求查询二级代理商资金校验模式</p>
<p>响应: OnRspQrySecAgentCheckMode</p>
<span class="anchor" id="aae54ac1-abe7-4883-9345-3f307f1a1aca"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) = 0;</p>
<span class="anchor" id="f927f795-8625-408b-bce3-ae0c004a3f0c"></span>
## 2.参数
<p>pQrySecAgentCheckMode：查询二级代理商资金校验模式</p>
<pre><code>struct CThostFtdcQrySecAgentCheckModeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="15cb1cbe-ad8f-48a3-a657-09839139e12c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="aa29288f-1650-4f76-a91d-6af5c4b7ca17"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="96017c9c-bdd6-484a-be12-80a55678797d"></span>
## 5.FAQ
<p>无</p>
