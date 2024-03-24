<p>请求查询产品报价汇率</p>
<p>响应: OnRspQryProductExchRate</p>
<span class="anchor" id="c40cb68c-6c0b-43c2-8e97-70f255e3486f"></span>
## 1.函数原型
<p>virtual int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) = 0;</p>
<span class="anchor" id="e02f3ba6-d548-4a23-9301-eb22965ffcc0"></span>
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
<span class="anchor" id="35f2beaf-a591-4f73-82a1-f441af0e8793"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1ebf0361-e834-425b-8437-0cbaf62a5143"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="efa45252-ac86-437d-866f-66caf1b1d37a"></span>
## 5.FAQ
<p>无</p>
