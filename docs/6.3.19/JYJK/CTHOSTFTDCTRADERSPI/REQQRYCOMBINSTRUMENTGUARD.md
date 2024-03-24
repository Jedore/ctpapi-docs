<p>请求查询组合合约安全系数</p>
<p>响应：OnRspQryCombInstrumentGuard</p>
<span class="anchor" id="d554d0bb-30bc-44e5-a118-f49e3e08eb85"></span>
## 1.函数原型
<p>virtual int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) = 0;</p>
<span class="anchor" id="a90ae67a-b8f3-4516-ac5a-5334be9e579b"></span>
## 2.参数
<p>pQryCombInstrumentGuard：组合合约安全系数查询</p>
<pre><code>struct CThostFtdcQryCombInstrumentGuardField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="66620577-4be9-498b-8806-2b7d87ee461c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e7b4ed5e-8a64-49d2-9515-476bb50c7901"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="3c1ca694-c95d-411e-88c4-c7469f571399"></span>
## 5.FAQ
<p>无</p>
