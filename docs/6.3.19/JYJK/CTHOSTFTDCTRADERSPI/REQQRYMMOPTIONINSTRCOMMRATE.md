<p>请求查询做市商期权合约手续费</p>
<p>响应: OnRspQryMMOptionInstrCommRate</p>
<span class="anchor" id="bc041aa8-5771-4076-91ec-26e8ae47df81"></span>
## 1.函数原型
<p>virtual int ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="e0d8cd3f-6522-45dd-a6cf-931698c03f0a"></span>
## 2.参数
<p>pQryMMOptionInstrCommRate：做市商期权手续费率查询</p>
<pre><code>struct CThostFtdcQryMMOptionInstrCommRateField
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
<span class="anchor" id="cd32a948-d191-4c4f-9412-e60fd3b6b70a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0394e454-92e8-4bda-83b8-7331af39af6f"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="20c99d6b-ad10-4434-8f61-11c6358e54b6"></span>
## 5.FAQ
<p>无</p>
