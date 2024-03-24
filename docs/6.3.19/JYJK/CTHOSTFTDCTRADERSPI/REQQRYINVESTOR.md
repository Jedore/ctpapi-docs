<p>请求查询投资者</p>
<p>响应：OnRspQryInvestor</p>
<span class="anchor" id="8eb80b15-0dd7-4b0c-8b2e-2776f2a9b2c2"></span>
## 1.函数原型
<p>virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;</p>
<span class="anchor" id="a6afe92f-ea52-4efa-9cd4-770c48f2cc7c"></span>
## 2.参数
<p>pQryInvestor：查询投资者</p>
<pre><code>struct CThostFtdcQryInvestorField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="4e187795-c62e-4b08-8a50-e1af15f01bb8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f09384ab-645e-44da-a4e2-de68e9e8ffa1"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryInvestor(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="608bbb86-bca7-4463-bb10-1906e9784ba6"></span>
## 5.FAQ
<p>无</p>
