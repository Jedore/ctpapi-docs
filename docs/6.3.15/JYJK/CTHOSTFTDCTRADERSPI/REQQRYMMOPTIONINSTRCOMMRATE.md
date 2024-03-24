<p>请求查询做市商期权合约手续费</p>
<p>响应: OnRspQryMMOptionInstrCommRate</p>
<span class="anchor" id="8af0ac5f-e683-4938-8d86-c3fcbe1e1b5b"></span>
## 1.函数原型
<p>virtual int ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="fcaa3bdd-7f56-4387-b02f-9f785cb3fd3b"></span>
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
<span class="anchor" id="662fc8db-a447-4733-b793-acfb778db8ae"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f03e5c12-2f07-4d11-96cb-39ccd6cdefda"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="381ebfe9-084b-4918-beb4-a65ff58ffd1c"></span>
## 5.FAQ
<p>无</p>
