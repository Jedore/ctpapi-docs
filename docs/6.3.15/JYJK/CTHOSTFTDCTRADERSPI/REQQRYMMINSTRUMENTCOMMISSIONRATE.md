<p>请求查询做市商合约手续费率</p>
<p>响应: OnRspQryMMInstrumentCommissionRate</p>
<span class="anchor" id="d552e187-373e-4d92-b8e7-a4c6504b83a0"></span>
## 1.函数原型
<p>virtual int ReqQryMMInstrumentCommissionRate(CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID) = 0;</p>
<span class="anchor" id="f6dc19ae-2a34-4ffb-9719-99f1746695f3"></span>
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
<span class="anchor" id="28928228-f134-4273-9a63-013f4efb2fa8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="cb77a4a7-15c4-4088-80bc-a7a0c34a2564"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="001e4e55-0419-462d-90f3-6490cd431be7"></span>
## 5.FAQ
<p>无</p>
