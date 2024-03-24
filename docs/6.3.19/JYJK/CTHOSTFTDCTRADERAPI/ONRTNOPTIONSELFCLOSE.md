<p>期权自对冲通知，当执行ReqOptionSelfCloseInsert后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="a782cb9d-2d08-4632-9520-d650022b56ef"></span>
## 1.函数原型
<p>virtual void OnRtnOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose) {};</p>
<span class="anchor" id="84e24703-bf73-45d9-905e-d98c2ff11514"></span>
## 2.参数
<p>pOptionSelfClose：期权自对冲</p>
<pre><code>struct CThostFtdcOptionSelfCloseField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///期权自对冲引用
    TThostFtdcOrderRefType OptionSelfCloseRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///数量
    TThostFtdcVolumeType Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权行权的头寸是否自对冲
    TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;
    ///本地期权自对冲编号
    TThostFtdcOrderLocalIDType OptionSelfCloseLocalID;
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
    ///期权自对冲提交状态
    TThostFtdcOrderSubmitStatusType OrderSubmitStatus;
    ///报单提示序号
    TThostFtdcSequenceNoType NotifySequence;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///期权自对冲编号
    TThostFtdcOrderSysIDType OptionSelfCloseSysID;
    ///报单日期
    TThostFtdcDateType InsertDate;
    ///插入时间
    TThostFtdcTimeType InsertTime;
    ///撤销时间
    TThostFtdcTimeType CancelTime;
    ///自对冲结果
    TThostFtdcExecResultType ExecResult;
    ///结算会员编号
    TThostFtdcParticipantIDType ClearingPartID;
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
    ///操作用户代码
    TThostFtdcUserIDType ActiveUserID;
    ///经纪公司报单编号
    TThostFtdcSequenceNoType BrokerOptionSelfCloseSeq;
    ///营业部编号
    TThostFtdcBranchIDType BranchID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>InstallID：CTP内部使用</p>
<p>OrderSubmitStatus：报单报入状态</p>
<p>ExecResult：最后的结果，检查是否自对冲成功</p>
<p>StatusMsg：错误信息</p>
<span class="anchor" id="ae830dec-2a86-461b-a107-6d2f5e72cba8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1f6522e7-bde2-49a8-b47b-554dd0e134ad"></span>
## 4.FAQ
<p>无</p>
