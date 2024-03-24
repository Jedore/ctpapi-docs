<p>查询最大报单数量响应，当执行ReqQueryMaxOrderVolume后，该方法被调用。</p>
<span class="anchor" id="a609dce3-104b-44e3-a462-88457d56439c"></span>
## 1.函数原型
<p>virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0d0adb35-4224-4325-993c-5819c445d64c"></span>
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
<p>MaxVolume：返回的是期货公司设置的合约最大报单数量，若超出交易所设置的则返回交易所的报错</p>
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
<span class="anchor" id="dbd57e66-cc9c-462b-b667-3dfe683f9c98"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="166ddcd3-eb1c-4e76-8c8a-a1232dcb1f7d"></span>
## 4.FAQ
<p>无</p>
