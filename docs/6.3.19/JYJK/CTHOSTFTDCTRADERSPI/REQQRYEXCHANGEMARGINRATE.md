<p>请求查询交易所保证金率</p>
<p>响应: OnRspQryExchangeMarginRate</p>
<span class="anchor" id="d22a99cf-080c-4eff-b236-66fb41ea9495"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) = 0;</p>
<span class="anchor" id="267584b1-172d-409f-bedf-359a459e1862"></span>
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
<span class="anchor" id="c511d223-1ec7-4a9d-bc7e-364090d2ebf7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d06ac6e8-06b4-40a5-a29a-dc70dc8ed064"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="43a436ee-6fe9-465e-a418-4cb4571922e7"></span>
## 5.FAQ
<p>无</p>
