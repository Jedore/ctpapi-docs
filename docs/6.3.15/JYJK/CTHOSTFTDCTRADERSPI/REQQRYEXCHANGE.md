<p>请求查询交易所</p>
<p>响应: OnRspQryExchange</p>
<span class="anchor" id="2579ac93-6672-4711-9149-bccb1ffeb3dc"></span>
## 1.函数原型
<p>virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;</p>
<span class="anchor" id="fcfa1f16-2c2f-4b84-b40d-bad1e1db3466"></span>
## 2.参数
<p>pQryExchange：查询交易所</p>
<pre><code>struct CThostFtdcQryExchangeField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="ad2c785b-44e8-496b-bf85-adfb1e7abeb8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0e0bdd47-beb3-4309-a829-0cb8c4bd4a82"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a47e05ae-ada9-410a-bcda-f2456d2ea9f7"></span>
## 5.FAQ
<p>无</p>
