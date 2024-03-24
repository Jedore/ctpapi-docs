<p>请求查询仓单折抵信息</p>
<p>响应: OnRspQryEWarrantOffset</p>
<span class="anchor" id="c720d4cb-5e2f-4337-b7ee-7c904df6189a"></span>
## 1.函数原型
<p>virtual int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) = 0;</p>
<span class="anchor" id="c2c0df95-e551-4663-9348-edd05fc02b40"></span>
## 2.参数
<p>pQryEWarrantOffset：查询仓单折抵信息</p>
<pre><code>struct CThostFtdcQryEWarrantOffsetField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="2d71df4e-bfd2-4996-8bdb-f5fb10eb7a48"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1bd5da5c-128e-4399-bd46-43d45d570d0d"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="299c88a5-eed5-4c0b-bdb8-bb8d9c32c28f"></span>
## 5.FAQ
<p>无</p>
