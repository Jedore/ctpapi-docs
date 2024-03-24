<p>申请组合通知，当执行ReqCombActionInsert后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="e68ccc09-676d-4c32-bc01-91e57175ee2e"></span>
## 1.函数原型
<p>virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) {};</p>
<span class="anchor" id="94706198-4380-4bc6-aa5d-60d5e86d22e1"></span>
## 2.参数
<p>pCombAction：申请组合</p>
<pre><code>struct CThostFtdcCombActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///组合引用
    TThostFtdcOrderRefType CombActionRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///数量
    TThostFtdcVolumeType Volume;
    ///组合指令方向
    TThostFtdcCombDirectionType CombDirection;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///本地申请组合编号
    TThostFtdcOrderLocalIDType ActionLocalID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///组合状态
    TThostFtdcOrderActionStatusType ActionStatus;
    ///报单提示序号
    TThostFtdcSequenceNoType NotifySequence;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///序号
    TThostFtdcSequenceNoType SequenceNo;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///用户端产品信息
    TThostFtdcProductInfoType UserProductInfo;
    ///状态信息
    TThostFtdcErrorMsgType StatusMsg;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
    ///组合编号
    TThostFtdcTradeIDType ComTradeID;
    ///营业部编号
    TThostFtdcBranchIDType BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>InstallID：CTP内部使用</p>
<p>ActionStatus：报入组合后的报单状态</p>
<span class="anchor" id="004227a0-3649-42bc-abee-9d2dc1f4d13a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8785eacd-e808-4ac6-915d-7d433045417c"></span>
## 4.FAQ
<p>无</p>
