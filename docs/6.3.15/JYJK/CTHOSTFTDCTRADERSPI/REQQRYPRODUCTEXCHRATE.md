<p>请求查询产品报价汇率</p>
<p>响应: OnRspQryProductExchRate</p>
<span class="anchor" id="9007c763-ee98-45df-9021-becd78166a98"></span>
## 1.函数原型
<p>virtual int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) = 0;</p>
<span class="anchor" id="b5aeec6c-b0f9-4239-9ccc-44fc45e2223d"></span>
## 2.参数
<p>pQryProductExchRate：产品报价汇率查询</p>
<pre><code>struct CThostFtdcQryProductExchRateField
{
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="fa86c2a3-b45a-44b5-9e99-0dc78e4fc67f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cb754c23-2f9f-4ff9-ab58-5a7c7f50bc67"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="87b346d7-bbec-4267-a224-1154920cb325"></span>
## 5.FAQ
<p>无</p>
