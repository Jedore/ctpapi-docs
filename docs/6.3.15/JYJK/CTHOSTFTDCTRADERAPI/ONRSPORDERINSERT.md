<p>报单录入请求响应，当执行ReqOrderInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="d7b5c7e2-1347-4af2-97db-fbf33703fd97"></span>
## 1.函数原型
<p>virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="35eff3e1-24e7-491a-992d-a1160bf143b2"></span>
## 2.参数
<p>pInputOrder：输入报单</p>
<pre><code>struct CThostFtdcInputOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///报单引用
    TThostFtdcOrderRefType OrderRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///报单价格条件
    TThostFtdcOrderPriceTypeType OrderPriceType;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///组合开平标志
    TThostFtdcCombOffsetFlagType CombOffsetFlag;
    ///组合投机套保标志
    TThostFtdcCombHedgeFlagType CombHedgeFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量
    TThostFtdcVolumeType VolumeTotalOriginal;
    ///有效期类型
    TThostFtdcTimeConditionType TimeCondition;
    ///GTD日期
    TThostFtdcDateType GTDDate;
    ///成交量类型
    TThostFtdcVolumeConditionType VolumeCondition;
    ///最小成交量
    TThostFtdcVolumeType MinVolume;
    ///触发条件
    TThostFtdcContingentConditionType ContingentCondition;
    ///止损价
    TThostFtdcPriceType StopPrice;
    ///强平原因
    TThostFtdcForceCloseReasonType ForceCloseReason;
    ///自动挂起标志
    TThostFtdcBoolType IsAutoSuspend;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///用户强评标志
    TThostFtdcBoolType UserForceClose;
    ///互换单标志
    TThostFtdcBoolType IsSwapOrder;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
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
<span class="anchor" id="3917682b-c9c8-4ea6-94d7-f56bff67ba58"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4b12e185-5fa2-4383-b332-7936f16ba603"></span>
## 4.FAQ
<p>无</p>
