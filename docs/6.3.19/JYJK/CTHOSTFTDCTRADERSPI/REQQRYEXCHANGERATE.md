<p>请求查询汇率</p>
<p>响应：OnRspQryExchangeRate</p>
<span class="anchor" id="774804e9-f0d8-4352-ab5d-2fd4258a47aa"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) = 0;</p>
<span class="anchor" id="d1dae4f9-ff9e-4748-8764-4a7be76bb0c8"></span>
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
<span class="anchor" id="ace24507-6675-47b9-82f0-5deb26c090b9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="50aeaa8a-9525-4e43-a54f-c5ac91acfaa6"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8da3b82a-0841-487d-8b48-f01101fcf0b5"></span>
## 5.FAQ
<p>无</p>
