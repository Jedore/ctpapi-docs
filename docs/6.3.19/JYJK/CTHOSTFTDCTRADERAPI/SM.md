<p>查询最大报单数量响应，当执行ReqQueryMaxOrderVolume后，该方法被调用。</p>
<span class="anchor" id="428738c7-7524-42ea-a4d8-2cfee11604ba"></span>
## 1.函数原型
<p>virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="bc63df21-0926-4f96-98ea-95b41db3ec8c"></span>
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
<span class="anchor" id="ae17dad1-938b-490d-93f5-3923a05e8cf5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b92374fb-d299-4236-afc4-e9b45fe374fd"></span>
## 4.FAQ
<p>无</p>
