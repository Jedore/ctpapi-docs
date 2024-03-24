<p>请求查询交易所调整保证金率</p>
<p>响应: OnRspQryExchangeMarginRateAdjust</p>
<span class="anchor" id="c4486415-9ffb-4266-960b-874ec2e1230f"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID) = 0;</p>
<span class="anchor" id="11ddb44e-5550-47fa-80db-4ca790751f3c"></span>
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
<span class="anchor" id="79ddd0db-caa6-474c-b029-dce442f07c24"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="90cc3c99-c1d4-46e2-8013-7e6566c8ffa4"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b6746239-15b4-4ff6-b4cd-ea17afda11e8"></span>
## 5.FAQ
<p>无</p>
