<p>请求查询交易所保证金率</p>
<p>响应: OnRspQryExchangeMarginRate</p>
<span class="anchor" id="2a54b7e0-6ff6-4edb-8a31-d90f80a2e33b"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) = 0;</p>
<span class="anchor" id="379f6f84-fc9f-4e3f-9fa5-f25720a21fb5"></span>
## 2.参数
<p>pQryExchangeMarginRate：查询交易所保证金率</p>
<pre><code>struct CThostFtdcQryExchangeMarginRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="1f0b33d2-ac35-41b9-a1fa-d09ff0616da5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="eeae0022-0d15-4f1d-a60a-af1f4bd59ad2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="1b3494a3-ce7b-402b-828c-5d8e7f47f5d6"></span>
## 5.FAQ
<p>无</p>
