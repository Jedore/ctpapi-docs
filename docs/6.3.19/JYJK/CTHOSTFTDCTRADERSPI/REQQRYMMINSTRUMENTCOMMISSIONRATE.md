<p>请求查询做市商合约手续费率</p>
<p>响应: OnRspQryMMInstrumentCommissionRate</p>
<span class="anchor" id="236958c9-0414-4830-ab71-5d1e1aad34aa"></span>
## 1.函数原型
<p>virtual int ReqQryMMInstrumentCommissionRate(CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID) = 0;</p>
<span class="anchor" id="6d270768-c928-43df-8989-58eec06e316d"></span>
## 2.参数
<p>pQryMMInstrumentCommissionRate：查询做市商合约手续费率</p>
<pre><code>struct CThostFtdcQryMMInstrumentCommissionRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d7732f02-a7f1-4148-b167-702b3907600c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="693f3ba7-a784-4a32-8c99-7d01c2729504"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a5253a64-529f-44fd-8036-5533f9626199"></span>
## 5.FAQ
<p>无</p>
