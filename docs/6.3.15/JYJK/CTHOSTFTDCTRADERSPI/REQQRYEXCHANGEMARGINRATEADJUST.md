<p>请求查询交易所调整保证金率</p>
<p>响应: OnRspQryExchangeMarginRateAdjust</p>
<span class="anchor" id="32e006f2-c172-49ab-8afa-d38ad19ba377"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID) = 0;</p>
<span class="anchor" id="b5f9575d-95c7-4f1f-aebb-e1c282e13198"></span>
## 2.参数
<p>pQryExchangeMarginRateAdjust：查询交易所调整保证金率</p>
<pre><code>struct CThostFtdcQryExchangeMarginRateAdjustField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="93af5338-4e09-4d4e-b0d9-729377cc0b96"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="34bb641e-e0d0-45c8-bc55-d1d1955768a3"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8c80e897-aa8e-4d9b-b4fb-16dd4e3640ad"></span>
## 5.FAQ
<p>无</p>
