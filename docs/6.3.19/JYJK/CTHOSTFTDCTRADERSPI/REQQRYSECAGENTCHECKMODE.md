<p>请求查询二级代理商资金校验模式</p>
<p>响应: OnRspQrySecAgentCheckMode</p>
<span class="anchor" id="3d449527-c61e-4e8d-96c9-e59b0236b7f9"></span>
## 1.函数原型
<p>virtual int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) = 0;</p>
<span class="anchor" id="ebd56d6a-e4b5-40fd-9d32-75fd0a623e55"></span>
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
<span class="anchor" id="e46e6d68-f240-4b53-b0c5-1bc36f3082fc"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="19817d9f-8071-4ae6-990c-adfb4bdcd878"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ca9c4274-27d9-4935-adee-aa68789f8f7d"></span>
## 5.FAQ
<p>无</p>
