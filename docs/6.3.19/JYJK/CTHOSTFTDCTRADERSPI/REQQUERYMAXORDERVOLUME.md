<p>查询最大报单数量请求，对应响应OnRspQueryMaxOrderVolume。</p>
<p>虽然ReqQueryMaxOrderVolume可以查询可开，但是交易核心在计算的时候是没有算手续费的，所以不完全准，计算逻辑是按照昨结算价计算的可开；如果需要精确结果的，建议自行计算。另外，可平的查询是已经排除了冻结持仓的。</p>
<span class="anchor" id="cbc3fba6-f353-46f4-801c-e32ed4b4cd68"></span>
## 1.函数原型
<p>virtual int ReqQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) = 0;</p>
<span class="anchor" id="c11a6367-4562-44a0-8873-1ac15ff4c781"></span>
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
<p>MaxVolume：取值结果为，min（可开/可平，限价单最大下单量）；可开根据昨结算价计算得出。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="37498741-7f22-48ad-a124-0b4dd635b900"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2485f1d0-8cbb-4bcc-a828-be3c65497508"></span>
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
<span class="anchor" id="835d2422-5847-404d-a3c9-f3dfaacafe52"></span>
## 5.FAQ
<p>无</p>
