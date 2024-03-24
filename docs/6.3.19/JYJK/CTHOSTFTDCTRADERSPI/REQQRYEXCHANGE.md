<p>请求查询交易所</p>
<p>响应: OnRspQryExchange</p>
<span class="anchor" id="1372b2b1-1e1b-44f8-b40f-a8aad41aba52"></span>
## 1.函数原型
<p>virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;</p>
<span class="anchor" id="4cb21e3c-06be-4deb-8634-ff133777bc4c"></span>
## 2.参数
<p>pQryExchange：查询交易所</p>
<pre><code>struct CThostFtdcQryExchangeField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="014ce6bd-babf-47e1-96c8-8a2c9db80d5e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cd3c28f8-3e14-4bfb-88e4-c991abc941bc"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0e7ceb20-8f44-4e23-b805-5c36c9b0401f"></span>
## 5.FAQ
<p>无</p>
