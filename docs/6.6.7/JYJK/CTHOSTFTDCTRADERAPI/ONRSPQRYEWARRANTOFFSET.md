<p>请求查询仓单折抵信息响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEWARRANTOFFSET/">ReqQryEWarrantOffset</a>后，该方法被调用。</p>
<span class="anchor" id="2700359d-68fd-40e0-848a-6feab2ff2f39"></span>
## 1.函数原型
<p>virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f49277b3-e195-4e5c-9ef7-be2334d37463"></span>
## 2.参数
<p>pEWarrantOffset：仓单折抵信息</p>
<pre><code>struct CThostFtdcEWarrantOffsetField
{
    ///交易日期
    TThostFtdcTradeDateType TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="63e9a10c-06c4-4b89-836e-adbd434ee2c3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4eb608e3-823d-4238-8176-264c4cfc0c47"></span>
## 4.FAQ
<p>无</p>
