<p>请求查询汇率</p>
<p>响应：OnRspQryExchangeRate</p>
<span class="anchor" id="d18cc83d-c6cb-4914-a949-76d504b301a4"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) = 0;</p>
<span class="anchor" id="66e2be77-17f9-4ffc-beb4-9f8edb132f25"></span>
## 2.参数
<p>pQryExchangeRate：查询汇率</p>
<pre><code>struct CThostFtdcQryExchangeRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///源币种
    TThostFtdcCurrencyIDType FromCurrencyID;
    ///目标币种
    TThostFtdcCurrencyIDType ToCurrencyID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="cb150a8c-3859-4def-97b6-dc48cd62e4b2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="af89615e-f9c4-417f-b517-cd98ad39fed3"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2f14ec71-43d3-4b7b-9d60-47e82f5a22d0"></span>
## 5.FAQ
<p>无</p>
