<p>请求查询投资者</p>
<p>响应：OnRspQryInvestor</p>
<span class="anchor" id="70d9e7fd-9845-4c82-97b9-fba8b6d4e848"></span>
## 1.函数原型
<p>virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;</p>
<span class="anchor" id="179123ca-a82b-4881-b7d0-59c857fedea6"></span>
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
<span class="anchor" id="c77283bf-b917-4155-b5f3-f28e76a7b8a9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="df40b0a9-b566-432a-8c06-70dbc4178f01"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
m_pUserApi-&gt;ReqQryInvestor(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="0a42d088-a61b-41a8-b5e4-fb1bd77b537f"></span>
## 5.FAQ
<p>无</p>
