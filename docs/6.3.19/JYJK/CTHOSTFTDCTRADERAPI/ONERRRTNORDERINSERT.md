<p>报单录入错误回报，当执行ReqOrderInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="b107ac7b-bc68-4fac-8c5b-99ea2fb4f9d9"></span>
## 1.函数原型
<p>virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="c000a392-a4fa-4770-8286-b5cf3058f9ae"></span>
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
<span class="anchor" id="0ad282fc-a142-450c-b8e1-406ed848288f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6ca925a7-c1d8-4220-92da-40bb115fcbe5"></span>
## 4.FAQ
<p>无</p>
