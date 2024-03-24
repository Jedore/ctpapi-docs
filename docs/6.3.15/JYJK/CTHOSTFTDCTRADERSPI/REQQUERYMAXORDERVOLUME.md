<p>查询最大报单数量请求，对应响应OnRspQueryMaxOrderVolume。</p>
<p>虽然ReqQueryMaxOrderVolume可以查询可开，但是交易核心在计算的时候是没有算手续费的，所以不完全准；如果需要精确结果的，建议自行计算。另外，可平的查询是已经排除了冻结持仓的。</p>
<span class="anchor" id="aef9f197-1c9e-4007-a6d9-2b7f15b0f40f"></span>
## 1.函数原型
<p>virtual int ReqQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) = 0;</p>
<span class="anchor" id="effa2c39-421e-49da-8248-eaad00d51b92"></span>
## 2.参数
<p>pQueryMaxOrderVolume：查询最大报单数量</p>
<pre><code>struct CThostFtdcQueryMaxOrderVolumeField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///开平标志
    TThostFtdcOffsetFlagType OffsetFlag;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///最大允许报单数量
    TThostFtdcVolumeType MaxVolume;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="68929933-4fc5-4e1a-8127-482a9beb9f36"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ddde6ea4-f26c-4369-a495-106b08890b69"></span>
## 4.调用示例
<pre><code>CThostFtdcQueryMaxOrderVolumeField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
a.Direction = THOST_FTDC_D_Buy;
a.OffsetFlag = THOST_FTDC_OF_Open;
a.HedgeFlag = THOST_FTDC_HF_Speculation;
a.MaxVolume = 1;
strcpy_s(a.BrokerID, "9999");
m_pUserApi-&gt;ReqQueryMaxOrderVolume(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="9767195f-6ff4-4995-8884-42e1777dd8b1"></span>
## 5.FAQ
<p>无</p>
