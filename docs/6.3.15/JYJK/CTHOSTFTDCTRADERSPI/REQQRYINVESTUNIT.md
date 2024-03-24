<p>请求查询投资单元</p>
<p>响应: OnRspQryInvestUnit</p>
<span class="anchor" id="47a7fcba-b2bd-44dc-938e-ed4bce141272"></span>
## 1.函数原型
<p>virtual int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) = 0;</p>
<span class="anchor" id="8d28e6af-8f07-420d-9a1b-35ec2a7e7fab"></span>
## 2.参数
<p>pQryInvestUnit：查询投资单元</p>
<pre><code>struct CThostFtdcQryInvestUnitField
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
<span class="anchor" id="8864b048-8968-4fc8-ae95-e5ca2e9c9e2b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3fb5f2b0-c07b-4b86-a4c1-aff2161c2e1a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="6cdf8273-65a6-4f04-a813-614ef8363a19"></span>
## 5.FAQ
<p>无</p>
