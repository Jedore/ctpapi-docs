<p>请求查询组合合约安全系数</p>
<p>响应：OnRspQryCombInstrumentGuard</p>
<span class="anchor" id="0a1a9ffa-36ba-4877-9d21-1912c96ac0c3"></span>
## 1.函数原型
<p>virtual int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) = 0;</p>
<span class="anchor" id="a29c7ae8-4c6f-4c7e-b67b-dd4d12dc9334"></span>
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
<span class="anchor" id="d4291971-1ccc-45ac-b759-5888693afcf9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7706ba40-0580-49b7-8a22-a4e80d387e63"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="286ee402-774c-4b83-bba4-2e97e896993e"></span>
## 5.FAQ
<p>无</p>
