#CTP常量定义
> CTPAPI 6.7.7

#### 1. ExchangePropertyType

交易所属性类型

`typedef char TThostFtdcExchangePropertyType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_EXP_Normal` | `'0'` |
| 根据成交生成报单 | `THOST_FTDC_EXP_GenOrderByTrade` | `'1'` |

#### 2. IdCardTypeType

证件类型类型

`typedef char TThostFtdcIdCardTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 组织机构代码 | `THOST_FTDC_ICT_EID` | `'0'` |
| 中国公民身份证 | `THOST_FTDC_ICT_IDCard` | `'1'` |
| 军官证 | `THOST_FTDC_ICT_OfficerIDCard` | `'2'` |
| 警官证 | `THOST_FTDC_ICT_PoliceIDCard` | `'3'` |
| 士兵证 | `THOST_FTDC_ICT_SoldierIDCard` | `'4'` |
| 护照 | `THOST_FTDC_ICT_Passport` | `'6'` |
| 回乡证 | `THOST_FTDC_ICT_HomeComingCard` | `'8'` |
| 营业执照号 | `THOST_FTDC_ICT_LicenseNo` | `'9'` |
| 税务登记号 | `THOST_FTDC_ICT_TaxNo` | `'A'` |
| 台湾居民来往大陆通行证 | `THOST_FTDC_ICT_TwMainlandTravelPermit` | `'C'` |
| 驾照 | `THOST_FTDC_ICT_DrivingLicense` | `'D'` |
| 当地社保ID | `THOST_FTDC_ICT_SocialID` | `'F'` |
| 当地身份证 | `THOST_FTDC_ICT_LocalID` | `'G'` |
| 港澳永久性居民身份证 | `THOST_FTDC_ICT_HKMCIDCard` | `'I'` |
| 人行开户许可证 | `THOST_FTDC_ICT_AccountsPermits` | `'J'` |
| 外国人永久居留证 | `THOST_FTDC_ICT_FrgPrmtRdCard` | `'K'` |
| 资管产品备案函 | `THOST_FTDC_ICT_CptMngPrdLetter` | `'L'` |
| 港澳台居民居住证 | `THOST_FTDC_ICT_HKMCTwResidencePermit` | `'M'` |
| 统一社会信用代码 | `THOST_FTDC_ICT_UniformSocialCreditCode` | `'N'` |
| 机构成立证明文件 | `THOST_FTDC_ICT_CorporationCertNo` | `'O'` |
| 其他证件 | `THOST_FTDC_ICT_OtherCard` | `'x'` |

#### 3. InvestorRangeType

投资者范围类型

`typedef char TThostFtdcInvestorRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有 | `THOST_FTDC_IR_All` | `'1'` |
| 投资者组 | `THOST_FTDC_IR_Group` | `'2'` |
| 单一投资者 | `THOST_FTDC_IR_Single` | `'3'` |

#### 4. DepartmentRangeType

投资者范围类型

`typedef char TThostFtdcDepartmentRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有 | `THOST_FTDC_DR_All` | `'1'` |
| 组织架构 | `THOST_FTDC_DR_Group` | `'2'` |
| 单一投资者 | `THOST_FTDC_DR_Single` | `'3'` |

#### 5. DataSyncStatusType

数据同步状态类型

`typedef char TThostFtdcDataSyncStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未同步 | `THOST_FTDC_DS_Asynchronous` | `'1'` |
| 同步中 | `THOST_FTDC_DS_Synchronizing` | `'2'` |
| 已同步 | `THOST_FTDC_DS_Synchronized` | `'3'` |

#### 6. BrokerDataSyncStatusType

经纪公司数据同步状态类型

`typedef char TThostFtdcBrokerDataSyncStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已同步 | `THOST_FTDC_BDS_Synchronized` | `'1'` |
| 同步中 | `THOST_FTDC_BDS_Synchronizing` | `'2'` |

#### 7. ExchangeConnectStatusType

交易所连接状态类型

`typedef char TThostFtdcExchangeConnectStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 没有任何连接 | `THOST_FTDC_ECS_NoConnection` | `'1'` |
| 已经发出合约查询请求 | `THOST_FTDC_ECS_QryInstrumentSent` | `'2'` |
| 已经获取信息 | `THOST_FTDC_ECS_GotInformation` | `'9'` |

#### 8. TraderConnectStatusType

交易所交易员连接状态类型

`typedef char TThostFtdcTraderConnectStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 没有任何连接 | `THOST_FTDC_TCS_NotConnected` | `'1'` |
| 已经连接 | `THOST_FTDC_TCS_Connected` | `'2'` |
| 已经发出合约查询请求 | `THOST_FTDC_TCS_QryInstrumentSent` | `'3'` |
| 订阅私有流 | `THOST_FTDC_TCS_SubPrivateFlow` | `'4'` |

#### 9. FunctionCodeType

功能代码类型

`typedef char TThostFtdcFunctionCodeType;`

|名称|宏定义|常量|
|--|--|--|
| 数据异步化 | `THOST_FTDC_FC_DataAsync` | `'1'` |
| 强制用户登出 | `THOST_FTDC_FC_ForceUserLogout` | `'2'` |
| 变更管理用户口令 | `THOST_FTDC_FC_UserPasswordUpdate` | `'3'` |
| 变更经纪公司口令 | `THOST_FTDC_FC_BrokerPasswordUpdate` | `'4'` |
| 变更投资者口令 | `THOST_FTDC_FC_InvestorPasswordUpdate` | `'5'` |
| 报单插入 | `THOST_FTDC_FC_OrderInsert` | `'6'` |
| 报单操作 | `THOST_FTDC_FC_OrderAction` | `'7'` |
| 同步系统数据 | `THOST_FTDC_FC_SyncSystemData` | `'8'` |
| 同步经纪公司数据 | `THOST_FTDC_FC_SyncBrokerData` | `'9'` |
| 批量同步经纪公司数据 | `THOST_FTDC_FC_BachSyncBrokerData` | `'A'` |
| 超级查询 | `THOST_FTDC_FC_SuperQuery` | `'B'` |
| 预埋报单插入 | `THOST_FTDC_FC_ParkedOrderInsert` | `'C'` |
| 预埋报单操作 | `THOST_FTDC_FC_ParkedOrderAction` | `'D'` |
| 同步动态令牌 | `THOST_FTDC_FC_SyncOTP` | `'E'` |
| 删除未知单 | `THOST_FTDC_FC_DeleteOrder` | `'F'` |
| 退出紧急状态 | `THOST_FTDC_FC_ExitEmergency` | `'G'` |

#### 10. BrokerFunctionCodeType

经纪公司功能代码类型

`typedef char TThostFtdcBrokerFunctionCodeType;`

|名称|宏定义|常量|
|--|--|--|
| 强制用户登出 | `THOST_FTDC_BFC_ForceUserLogout` | `'1'` |
| 变更用户口令 | `THOST_FTDC_BFC_UserPasswordUpdate` | `'2'` |
| 同步经纪公司数据 | `THOST_FTDC_BFC_SyncBrokerData` | `'3'` |
| 批量同步经纪公司数据 | `THOST_FTDC_BFC_BachSyncBrokerData` | `'4'` |
| 报单插入 | `THOST_FTDC_BFC_OrderInsert` | `'5'` |
| 报单操作 | `THOST_FTDC_BFC_OrderAction` | `'6'` |
| 全部查询 | `THOST_FTDC_BFC_AllQuery` | `'7'` |
| 系统功能：登入 | `THOST_FTDC_BFC_log` | `'a'` |
| 基本查询：查询基础数据，如合约，交易所等常量 | `THOST_FTDC_BFC_BaseQry` | `'b'` |
| 交易查询：如查成交，委托 | `THOST_FTDC_BFC_TradeQry` | `'c'` |
| 交易功能：报单，撤单 | `THOST_FTDC_BFC_Trade` | `'d'` |
| 银期转账 | `THOST_FTDC_BFC_Virement` | `'e'` |
| 风险监控 | `THOST_FTDC_BFC_Risk` | `'f'` |
| 查询 | `THOST_FTDC_BFC_Session` | `'g'` |
| 风控通知控制 | `THOST_FTDC_BFC_RiskNoticeCtl` | `'h'` |
| 风控通知发送 | `THOST_FTDC_BFC_RiskNotice` | `'i'` |
| 察看经纪公司资金权限 | `THOST_FTDC_BFC_BrokerDeposit` | `'j'` |
| 资金查询 | `THOST_FTDC_BFC_QueryFund` | `'k'` |
| 报单查询 | `THOST_FTDC_BFC_QueryOrder` | `'l'` |
| 成交查询 | `THOST_FTDC_BFC_QueryTrade` | `'m'` |
| 持仓查询 | `THOST_FTDC_BFC_QueryPosition` | `'n'` |
| 行情查询 | `THOST_FTDC_BFC_QueryMarketData` | `'o'` |
| 用户事件查询 | `THOST_FTDC_BFC_QueryUserEvent` | `'p'` |
| 风险通知查询 | `THOST_FTDC_BFC_QueryRiskNotify` | `'q'` |
| 出入金查询 | `THOST_FTDC_BFC_QueryFundChange` | `'r'` |
| 投资者信息查询 | `THOST_FTDC_BFC_QueryInvestor` | `'s'` |
| 交易编码查询 | `THOST_FTDC_BFC_QueryTradingCode` | `'t'` |
| 强平 | `THOST_FTDC_BFC_ForceClose` | `'u'` |
| 压力测试 | `THOST_FTDC_BFC_PressTest` | `'v'` |
| 权益反算 | `THOST_FTDC_BFC_RemainCalc` | `'w'` |
| 净持仓保证金指标 | `THOST_FTDC_BFC_NetPositionInd` | `'x'` |
| 风险预算 | `THOST_FTDC_BFC_RiskPredict` | `'y'` |
| 数据导出 | `THOST_FTDC_BFC_DataExport` | `'z'` |
| 风控指标设置 | `THOST_FTDC_BFC_RiskTargetSetup` | `'A'` |
| 行情预警 | `THOST_FTDC_BFC_MarketDataWarn` | `'B'` |
| 业务通知查询 | `THOST_FTDC_BFC_QryBizNotice` | `'C'` |
| 业务通知模板设置 | `THOST_FTDC_BFC_CfgBizNotice` | `'D'` |
| 同步动态令牌 | `THOST_FTDC_BFC_SyncOTP` | `'E'` |
| 发送业务通知 | `THOST_FTDC_BFC_SendBizNotice` | `'F'` |
| 风险级别标准设置 | `THOST_FTDC_BFC_CfgRiskLevelStd` | `'G'` |
| 交易终端应急功能 | `THOST_FTDC_BFC_TbCommand` | `'H'` |
| 删除未知单 | `THOST_FTDC_BFC_DeleteOrder` | `'J'` |
| 预埋报单插入 | `THOST_FTDC_BFC_ParkedOrderInsert` | `'K'` |
| 预埋报单操作 | `THOST_FTDC_BFC_ParkedOrderAction` | `'L'` |
| 资金不够仍允许行权 | `THOST_FTDC_BFC_ExecOrderNoCheck` | `'M'` |
| 指定 | `THOST_FTDC_BFC_Designate` | `'N'` |
| 证券处置 | `THOST_FTDC_BFC_StockDisposal` | `'O'` |
| 席位资金预警 | `THOST_FTDC_BFC_BrokerDepositWarn` | `'Q'` |
| 备兑不足预警 | `THOST_FTDC_BFC_CoverWarn` | `'S'` |
| 行权试算 | `THOST_FTDC_BFC_PreExecOrder` | `'T'` |
| 行权交收风险 | `THOST_FTDC_BFC_ExecOrderRisk` | `'P'` |
| 持仓限额预警 | `THOST_FTDC_BFC_PosiLimitWarn` | `'U'` |
| 持仓限额查询 | `THOST_FTDC_BFC_QryPosiLimit` | `'V'` |
| 银期签到签退 | `THOST_FTDC_BFC_FBSign` | `'W'` |
| 银期签约解约 | `THOST_FTDC_BFC_FBAccount` | `'X'` |

#### 11. OrderActionStatusType

报单操作状态类型

`typedef char TThostFtdcOrderActionStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已经提交 | `THOST_FTDC_OAS_Submitted` | `'a'` |
| 已经接受 | `THOST_FTDC_OAS_Accepted` | `'b'` |
| 已经被拒绝 | `THOST_FTDC_OAS_Rejected` | `'c'` |

#### 12. OrderStatusType

报单状态类型

`typedef char TThostFtdcOrderStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 全部成交 | `THOST_FTDC_OST_AllTraded` | `'0'` |
| 部分成交还在队列中 | `THOST_FTDC_OST_PartTradedQueueing` | `'1'` |
| 部分成交不在队列中 | `THOST_FTDC_OST_PartTradedNotQueueing` | `'2'` |
| 未成交还在队列中 | `THOST_FTDC_OST_NoTradeQueueing` | `'3'` |
| 未成交不在队列中 | `THOST_FTDC_OST_NoTradeNotQueueing` | `'4'` |
| 撤单 | `THOST_FTDC_OST_Canceled` | `'5'` |
| 未知 | `THOST_FTDC_OST_Unknown` | `'a'` |
| 尚未触发 | `THOST_FTDC_OST_NotTouched` | `'b'` |
| 已触发 | `THOST_FTDC_OST_Touched` | `'c'` |

#### 13. OrderSubmitStatusType

报单提交状态类型

`typedef char TThostFtdcOrderSubmitStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已经提交 | `THOST_FTDC_OSS_InsertSubmitted` | `'0'` |
| 撤单已经提交 | `THOST_FTDC_OSS_CancelSubmitted` | `'1'` |
| 修改已经提交 | `THOST_FTDC_OSS_ModifySubmitted` | `'2'` |
| 已经接受 | `THOST_FTDC_OSS_Accepted` | `'3'` |
| 报单已经被拒绝 | `THOST_FTDC_OSS_InsertRejected` | `'4'` |
| 撤单已经被拒绝 | `THOST_FTDC_OSS_CancelRejected` | `'5'` |
| 改单已经被拒绝 | `THOST_FTDC_OSS_ModifyRejected` | `'6'` |

#### 14. PositionDateType

持仓日期类型

`typedef char TThostFtdcPositionDateType;`

|名称|宏定义|常量|
|--|--|--|
| 今日持仓 | `THOST_FTDC_PSD_Today` | `'1'` |
| 历史持仓 | `THOST_FTDC_PSD_History` | `'2'` |

#### 15. PositionDateTypeType

持仓日期类型类型

`typedef char TThostFtdcPositionDateTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 使用历史持仓 | `THOST_FTDC_PDT_UseHistory` | `'1'` |
| 不使用历史持仓 | `THOST_FTDC_PDT_NoUseHistory` | `'2'` |

#### 16. TradingRoleType

交易角色类型

`typedef char TThostFtdcTradingRoleType;`

|名称|宏定义|常量|
|--|--|--|
| 代理 | `THOST_FTDC_ER_Broker` | `'1'` |
| 自营 | `THOST_FTDC_ER_Host` | `'2'` |
| 做市商 | `THOST_FTDC_ER_Maker` | `'3'` |

#### 17. ProductClassType

产品类型类型

`typedef char TThostFtdcProductClassType;`

|名称|宏定义|常量|
|--|--|--|
| 期货 | `THOST_FTDC_PC_Futures` | `'1'` |
| 期货期权 | `THOST_FTDC_PC_Options` | `'2'` |
| 组合 | `THOST_FTDC_PC_Combination` | `'3'` |
| 即期 | `THOST_FTDC_PC_Spot` | `'4'` |
| 期转现 | `THOST_FTDC_PC_EFP` | `'5'` |
| 现货期权 | `THOST_FTDC_PC_SpotOption` | `'6'` |
| TAS合约 | `THOST_FTDC_PC_TAS` | `'7'` |
| 金属指数 | `THOST_FTDC_PC_MI` | `'I'` |

#### 18. APIProductClassType

产品类型类型

`typedef char TThostFtdcAPIProductClassType;`

|名称|宏定义|常量|
|--|--|--|
| 期货单一合约 | `THOST_FTDC_APC_FutureSingle` | `'1'` |
| 期权单一合约 | `THOST_FTDC_APC_OptionSingle` | `'2'` |
| 可交易期货(含期货组合和期货单一合约) | `THOST_FTDC_APC_Futures` | `'3'` |
| 可交易期权(含期权组合和期权单一合约) | `THOST_FTDC_APC_Options` | `'4'` |
| 可下单套利组合 | `THOST_FTDC_APC_TradingComb` | `'5'` |
| 可申请的组合（可以申请的组合合约 包含可以交易的合约） | `THOST_FTDC_APC_UnTradingComb` | `'6'` |
| 所有可以交易合约 | `THOST_FTDC_APC_AllTrading` | `'7'` |
| 所有合约（包含不能交易合约 慎用） | `THOST_FTDC_APC_All` | `'8'` |

#### 19. InstLifePhaseType

合约生命周期状态类型

`typedef char TThostFtdcInstLifePhaseType;`

|名称|宏定义|常量|
|--|--|--|
| 未上市 | `THOST_FTDC_IP_NotStart` | `'0'` |
| 上市 | `THOST_FTDC_IP_Started` | `'1'` |
| 停牌 | `THOST_FTDC_IP_Pause` | `'2'` |
| 到期 | `THOST_FTDC_IP_Expired` | `'3'` |

#### 20. DirectionType

买卖方向类型

`typedef char TThostFtdcDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 买 | `THOST_FTDC_D_Buy` | `'0'` |
| 卖 | `THOST_FTDC_D_Sell` | `'1'` |

#### 21. PositionTypeType

持仓类型类型

`typedef char TThostFtdcPositionTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 净持仓 | `THOST_FTDC_PT_Net` | `'1'` |
| 综合持仓 | `THOST_FTDC_PT_Gross` | `'2'` |

#### 22. PosiDirectionType

持仓多空方向类型

`typedef char TThostFtdcPosiDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 净 | `THOST_FTDC_PD_Net` | `'1'` |
| 多头 | `THOST_FTDC_PD_Long` | `'2'` |
| 空头 | `THOST_FTDC_PD_Short` | `'3'` |

#### 23. SysSettlementStatusType

系统结算状态类型

`typedef char TThostFtdcSysSettlementStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 不活跃 | `THOST_FTDC_SS_NonActive` | `'1'` |
| 启动 | `THOST_FTDC_SS_Startup` | `'2'` |
| 操作 | `THOST_FTDC_SS_Operating` | `'3'` |
| 结算 | `THOST_FTDC_SS_Settlement` | `'4'` |
| 结算完成 | `THOST_FTDC_SS_SettlementFinished` | `'5'` |

#### 24. RatioAttrType

费率属性类型

`typedef char TThostFtdcRatioAttrType;`

|名称|宏定义|常量|
|--|--|--|
| 交易费率 | `THOST_FTDC_RA_Trade` | `'0'` |
| 结算费率 | `THOST_FTDC_RA_Settlement` | `'1'` |

#### 25. HedgeFlagType

投机套保标志类型

`typedef char TThostFtdcHedgeFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 投机 | `THOST_FTDC_HF_Speculation` | `'1'` |
| 套利 | `THOST_FTDC_HF_Arbitrage` | `'2'` |
| 套保 | `THOST_FTDC_HF_Hedge` | `'3'` |
| 做市商 | `THOST_FTDC_HF_MarketMaker` | `'5'` |
| 第一腿投机第二腿套保 | `THOST_FTDC_HF_SpecHedge` | `'6'` |
| 第一腿套保第二腿投机 | `THOST_FTDC_HF_HedgeSpec` | `'7'` |

#### 26. BillHedgeFlagType

投机套保标志类型

`typedef char TThostFtdcBillHedgeFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 投机 | `THOST_FTDC_BHF_Speculation` | `'1'` |
| 套利 | `THOST_FTDC_BHF_Arbitrage` | `'2'` |
| 套保 | `THOST_FTDC_BHF_Hedge` | `'3'` |

#### 27. ClientIDTypeType

交易编码类型类型

`typedef char TThostFtdcClientIDTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 投机 | `THOST_FTDC_CIDT_Speculation` | `'1'` |
| 套利 | `THOST_FTDC_CIDT_Arbitrage` | `'2'` |
| 套保 | `THOST_FTDC_CIDT_Hedge` | `'3'` |
| 做市商 | `THOST_FTDC_CIDT_MarketMaker` | `'5'` |

#### 28. OrderPriceTypeType

报单价格条件类型

`typedef char TThostFtdcOrderPriceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 任意价 | `THOST_FTDC_OPT_AnyPrice` | `'1'` |
| 限价 | `THOST_FTDC_OPT_LimitPrice` | `'2'` |
| 最优价 | `THOST_FTDC_OPT_BestPrice` | `'3'` |
| 最新价 | `THOST_FTDC_OPT_LastPrice` | `'4'` |
| 最新价浮动上浮1个ticks | `THOST_FTDC_OPT_LastPricePlusOneTicks` | `'5'` |
| 最新价浮动上浮2个ticks | `THOST_FTDC_OPT_LastPricePlusTwoTicks` | `'6'` |
| 最新价浮动上浮3个ticks | `THOST_FTDC_OPT_LastPricePlusThreeTicks` | `'7'` |
| 卖一价 | `THOST_FTDC_OPT_AskPrice1` | `'8'` |
| 卖一价浮动上浮1个ticks | `THOST_FTDC_OPT_AskPrice1PlusOneTicks` | `'9'` |
| 卖一价浮动上浮2个ticks | `THOST_FTDC_OPT_AskPrice1PlusTwoTicks` | `'A'` |
| 卖一价浮动上浮3个ticks | `THOST_FTDC_OPT_AskPrice1PlusThreeTicks` | `'B'` |
| 买一价 | `THOST_FTDC_OPT_BidPrice1` | `'C'` |
| 买一价浮动上浮1个ticks | `THOST_FTDC_OPT_BidPrice1PlusOneTicks` | `'D'` |
| 买一价浮动上浮2个ticks | `THOST_FTDC_OPT_BidPrice1PlusTwoTicks` | `'E'` |
| 买一价浮动上浮3个ticks | `THOST_FTDC_OPT_BidPrice1PlusThreeTicks` | `'F'` |
| 五档价 | `THOST_FTDC_OPT_FiveLevelPrice` | `'G'` |

#### 29. OffsetFlagType

开平标志类型

`typedef char TThostFtdcOffsetFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 开仓 | `THOST_FTDC_OF_Open` | `'0'` |
| 平仓 | `THOST_FTDC_OF_Close` | `'1'` |
| 强平 | `THOST_FTDC_OF_ForceClose` | `'2'` |
| 平今 | `THOST_FTDC_OF_CloseToday` | `'3'` |
| 平昨 | `THOST_FTDC_OF_CloseYesterday` | `'4'` |
| 强减 | `THOST_FTDC_OF_ForceOff` | `'5'` |
| 本地强平 | `THOST_FTDC_OF_LocalForceClose` | `'6'` |

#### 30. ForceCloseReasonType

强平原因类型

`typedef char TThostFtdcForceCloseReasonType;`

|名称|宏定义|常量|
|--|--|--|
| 非强平 | `THOST_FTDC_FCC_NotForceClose` | `'0'` |
| 资金不足 | `THOST_FTDC_FCC_LackDeposit` | `'1'` |
| 客户超仓 | `THOST_FTDC_FCC_ClientOverPositionLimit` | `'2'` |
| 会员超仓 | `THOST_FTDC_FCC_MemberOverPositionLimit` | `'3'` |
| 持仓非整数倍 | `THOST_FTDC_FCC_NotMultiple` | `'4'` |
| 违规 | `THOST_FTDC_FCC_Violation` | `'5'` |
| 其它 | `THOST_FTDC_FCC_Other` | `'6'` |
| 自然人临近交割 | `THOST_FTDC_FCC_PersonDeliv` | `'7'` |
| 本地强平资金不足忽略敞口 | `THOST_FTDC_FCC_Notverifycapital` | `'8'` |
| 本地强平资金不足 | `THOST_FTDC_FCC_LocalLackDeposit` | `'9'` |
| 本地强平违规持仓忽略敞口 | `THOST_FTDC_FCC_LocalViolationNocheck` | `'a'` |
| 本地强平违规持仓 | `THOST_FTDC_FCC_LocalViolation` | `'b'` |

#### 31. OrderTypeType

报单类型类型

`typedef char TThostFtdcOrderTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_ORDT_Normal` | `'0'` |
| 报价衍生 | `THOST_FTDC_ORDT_DeriveFromQuote` | `'1'` |
| 组合衍生 | `THOST_FTDC_ORDT_DeriveFromCombination` | `'2'` |
| 组合报单 | `THOST_FTDC_ORDT_Combination` | `'3'` |
| 条件单 | `THOST_FTDC_ORDT_ConditionalOrder` | `'4'` |
| 互换单 | `THOST_FTDC_ORDT_Swap` | `'5'` |
| 大宗交易成交衍生 | `THOST_FTDC_ORDT_DeriveFromBlockTrade` | `'6'` |
| 期转现成交衍生 | `THOST_FTDC_ORDT_DeriveFromEFPTrade` | `'7'` |

#### 32. TimeConditionType

有效期类型类型

`typedef char TThostFtdcTimeConditionType;`

|名称|宏定义|常量|
|--|--|--|
| 立即完成，否则撤销 | `THOST_FTDC_TC_IOC` | `'1'` |
| 本节有效 | `THOST_FTDC_TC_GFS` | `'2'` |
| 当日有效 | `THOST_FTDC_TC_GFD` | `'3'` |
| 指定日期前有效 | `THOST_FTDC_TC_GTD` | `'4'` |
| 撤销前有效 | `THOST_FTDC_TC_GTC` | `'5'` |
| 集合竞价有效 | `THOST_FTDC_TC_GFA` | `'6'` |

#### 33. VolumeConditionType

成交量类型类型

`typedef char TThostFtdcVolumeConditionType;`

|名称|宏定义|常量|
|--|--|--|
| 任何数量 | `THOST_FTDC_VC_AV` | `'1'` |
| 最小数量 | `THOST_FTDC_VC_MV` | `'2'` |
| 全部数量 | `THOST_FTDC_VC_CV` | `'3'` |

#### 34. ContingentConditionType

触发条件类型

`typedef char TThostFtdcContingentConditionType;`

|名称|宏定义|常量|
|--|--|--|
| 立即 | `THOST_FTDC_CC_Immediately` | `'1'` |
| 止损 | `THOST_FTDC_CC_Touch` | `'2'` |
| 止赢 | `THOST_FTDC_CC_TouchProfit` | `'3'` |
| 预埋单 | `THOST_FTDC_CC_ParkedOrder` | `'4'` |
| 最新价大于条件价 | `THOST_FTDC_CC_LastPriceGreaterThanStopPrice` | `'5'` |
| 最新价大于等于条件价 | `THOST_FTDC_CC_LastPriceGreaterEqualStopPrice` | `'6'` |
| 最新价小于条件价 | `THOST_FTDC_CC_LastPriceLesserThanStopPrice` | `'7'` |
| 最新价小于等于条件价 | `THOST_FTDC_CC_LastPriceLesserEqualStopPrice` | `'8'` |
| 卖一价大于条件价 | `THOST_FTDC_CC_AskPriceGreaterThanStopPrice` | `'9'` |
| 卖一价大于等于条件价 | `THOST_FTDC_CC_AskPriceGreaterEqualStopPrice` | `'A'` |
| 卖一价小于条件价 | `THOST_FTDC_CC_AskPriceLesserThanStopPrice` | `'B'` |
| 卖一价小于等于条件价 | `THOST_FTDC_CC_AskPriceLesserEqualStopPrice` | `'C'` |
| 买一价大于条件价 | `THOST_FTDC_CC_BidPriceGreaterThanStopPrice` | `'D'` |
| 买一价大于等于条件价 | `THOST_FTDC_CC_BidPriceGreaterEqualStopPrice` | `'E'` |
| 买一价小于条件价 | `THOST_FTDC_CC_BidPriceLesserThanStopPrice` | `'F'` |
| 买一价小于等于条件价 | `THOST_FTDC_CC_BidPriceLesserEqualStopPrice` | `'H'` |

#### 35. ActionFlagType

操作标志类型

`typedef char TThostFtdcActionFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 删除 | `THOST_FTDC_AF_Delete` | `'0'` |
| 修改 | `THOST_FTDC_AF_Modify` | `'3'` |

#### 36. TradingRightType

交易权限类型

`typedef char TThostFtdcTradingRightType;`

|名称|宏定义|常量|
|--|--|--|
| 可以交易 | `THOST_FTDC_TR_Allow` | `'0'` |
| 只能平仓 | `THOST_FTDC_TR_CloseOnly` | `'1'` |
| 不能交易 | `THOST_FTDC_TR_Forbidden` | `'2'` |

#### 37. OrderSourceType

报单来源类型

`typedef char TThostFtdcOrderSourceType;`

|名称|宏定义|常量|
|--|--|--|
| 来自参与者 | `THOST_FTDC_OSRC_Participant` | `'0'` |
| 来自管理员 | `THOST_FTDC_OSRC_Administrator` | `'1'` |

#### 38. TradeTypeType

成交类型类型

`typedef char TThostFtdcTradeTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 组合持仓拆分为单一持仓,初始化不应包含该类型的持仓 | `THOST_FTDC_TRDT_SplitCombination` | `'#'` |
| 普通成交 | `THOST_FTDC_TRDT_Common` | `'0'` |
| 期权执行 | `THOST_FTDC_TRDT_OptionsExecution` | `'1'` |
| OTC成交 | `THOST_FTDC_TRDT_OTC` | `'2'` |
| 期转现衍生成交 | `THOST_FTDC_TRDT_EFPDerived` | `'3'` |
| 组合衍生成交 | `THOST_FTDC_TRDT_CombinationDerived` | `'4'` |
| 大宗交易成交 | `THOST_FTDC_TRDT_BlockTrade` | `'5'` |

#### 39. SpecPosiTypeType

特殊持仓明细标识类型

`typedef char TThostFtdcSpecPosiTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 普通持仓明细 | `THOST_FTDC_SPOST_Common` | `'#'` |
| TAS合约成交产生的标的合约持仓明细 | `THOST_FTDC_SPOST_Tas` | `'0'` |

#### 40. PriceSourceType

成交价来源类型

`typedef char TThostFtdcPriceSourceType;`

|名称|宏定义|常量|
|--|--|--|
| 前成交价 | `THOST_FTDC_PSRC_LastPrice` | `'0'` |
| 买委托价 | `THOST_FTDC_PSRC_Buy` | `'1'` |
| 卖委托价 | `THOST_FTDC_PSRC_Sell` | `'2'` |
| 场外成交价 | `THOST_FTDC_PSRC_OTC` | `'3'` |

#### 41. InstrumentStatusType

合约交易状态类型

`typedef char TThostFtdcInstrumentStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 开盘前 | `THOST_FTDC_IS_BeforeTrading` | `'0'` |
| 非交易 | `THOST_FTDC_IS_NoTrading` | `'1'` |
| 连续交易 | `THOST_FTDC_IS_Continous` | `'2'` |
| 集合竞价报单 | `THOST_FTDC_IS_AuctionOrdering` | `'3'` |
| 集合竞价价格平衡 | `THOST_FTDC_IS_AuctionBalance` | `'4'` |
| 集合竞价撮合 | `THOST_FTDC_IS_AuctionMatch` | `'5'` |
| 收盘 | `THOST_FTDC_IS_Closed` | `'6'` |
| 交易业务处理 | `THOST_FTDC_IS_TransactionProcessing` | `'7'` |

#### 42. InstStatusEnterReasonType

品种进入交易状态原因类型

`typedef char TThostFtdcInstStatusEnterReasonType;`

|名称|宏定义|常量|
|--|--|--|
| 自动切换 | `THOST_FTDC_IER_Automatic` | `'1'` |
| 手动切换 | `THOST_FTDC_IER_Manual` | `'2'` |
| 熔断 | `THOST_FTDC_IER_Fuse` | `'3'` |

#### 43. BatchStatusType

处理状态类型

`typedef char TThostFtdcBatchStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未上传 | `THOST_FTDC_BS_NoUpload` | `'1'` |
| 已上传 | `THOST_FTDC_BS_Uploaded` | `'2'` |
| 审核失败 | `THOST_FTDC_BS_Failed` | `'3'` |

#### 44. ReturnStyleType

按品种返还方式类型

`typedef char TThostFtdcReturnStyleType;`

|名称|宏定义|常量|
|--|--|--|
| 按所有品种 | `THOST_FTDC_RS_All` | `'1'` |
| 按品种 | `THOST_FTDC_RS_ByProduct` | `'2'` |

#### 45. ReturnPatternType

返还模式类型

`typedef char TThostFtdcReturnPatternType;`

|名称|宏定义|常量|
|--|--|--|
| 按成交手数 | `THOST_FTDC_RP_ByVolume` | `'1'` |
| 按留存手续费 | `THOST_FTDC_RP_ByFeeOnHand` | `'2'` |

#### 46. ReturnLevelType

返还级别类型

`typedef char TThostFtdcReturnLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 级别1 | `THOST_FTDC_RL_Level1` | `'1'` |
| 级别2 | `THOST_FTDC_RL_Level2` | `'2'` |
| 级别3 | `THOST_FTDC_RL_Level3` | `'3'` |
| 级别4 | `THOST_FTDC_RL_Level4` | `'4'` |
| 级别5 | `THOST_FTDC_RL_Level5` | `'5'` |
| 级别6 | `THOST_FTDC_RL_Level6` | `'6'` |
| 级别7 | `THOST_FTDC_RL_Level7` | `'7'` |
| 级别8 | `THOST_FTDC_RL_Level8` | `'8'` |
| 级别9 | `THOST_FTDC_RL_Level9` | `'9'` |

#### 47. ReturnStandardType

返还标准类型

`typedef char TThostFtdcReturnStandardType;`

|名称|宏定义|常量|
|--|--|--|
| 分阶段返还 | `THOST_FTDC_RSD_ByPeriod` | `'1'` |
| 按某一标准 | `THOST_FTDC_RSD_ByStandard` | `'2'` |

#### 48. MortgageTypeType

质押类型类型

`typedef char TThostFtdcMortgageTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 质出 | `THOST_FTDC_MT_Out` | `'0'` |
| 质入 | `THOST_FTDC_MT_In` | `'1'` |

#### 49. InvestorSettlementParamIDType

投资者结算参数代码类型

`typedef char TThostFtdcInvestorSettlementParamIDType;`

|名称|宏定义|常量|
|--|--|--|
| 质押比例 | `THOST_FTDC_ISPI_MortgageRatio` | `'4'` |
| 保证金算法 | `THOST_FTDC_ISPI_MarginWay` | `'5'` |
| 结算单结存是否包含质押 | `THOST_FTDC_ISPI_BillDeposit` | `'9'` |

#### 50. ExchangeSettlementParamIDType

交易所结算参数代码类型

`typedef char TThostFtdcExchangeSettlementParamIDType;`

|名称|宏定义|常量|
|--|--|--|
| 质押比例 | `THOST_FTDC_ESPI_MortgageRatio` | `'1'` |
| 分项资金导入项 | `THOST_FTDC_ESPI_OtherFundItem` | `'2'` |
| 分项资金入交易所出入金 | `THOST_FTDC_ESPI_OtherFundImport` | `'3'` |
| 中金所开户最低可用金额 | `THOST_FTDC_ESPI_CFFEXMinPrepa` | `'6'` |
| 郑商所结算方式 | `THOST_FTDC_ESPI_CZCESettlementType` | `'7'` |
| 交易所交割手续费收取方式 | `THOST_FTDC_ESPI_ExchDelivFeeMode` | `'9'` |
| 投资者交割手续费收取方式 | `THOST_FTDC_ESPI_DelivFeeMode` | `'0'` |
| 郑商所组合持仓保证金收取方式 | `THOST_FTDC_ESPI_CZCEComMarginType` | `'A'` |
| 大商所套利保证金是否优惠 | `THOST_FTDC_ESPI_DceComMarginType` | `'B'` |
| 虚值期权保证金优惠比率 | `THOST_FTDC_ESPI_OptOutDisCountRate` | `'a'` |
| 最低保障系数 | `THOST_FTDC_ESPI_OptMiniGuarantee` | `'b'` |

#### 51. SystemParamIDType

系统参数代码类型

`typedef char TThostFtdcSystemParamIDType;`

|名称|宏定义|常量|
|--|--|--|
| 投资者代码最小长度 | `THOST_FTDC_SPI_InvestorIDMinLength` | `'1'` |
| 投资者帐号代码最小长度 | `THOST_FTDC_SPI_AccountIDMinLength` | `'2'` |
| 投资者开户默认登录权限 | `THOST_FTDC_SPI_UserRightLogon` | `'3'` |
| 投资者交易结算单成交汇总方式 | `THOST_FTDC_SPI_SettlementBillTrade` | `'4'` |
| 统一开户更新交易编码方式 | `THOST_FTDC_SPI_TradingCode` | `'5'` |
| 结算是否判断存在未复核的出入金和分项资金 | `THOST_FTDC_SPI_CheckFund` | `'6'` |
| 是否启用手续费模板数据权限 | `THOST_FTDC_SPI_CommModelRight` | `'7'` |
| 是否启用保证金率模板数据权限 | `THOST_FTDC_SPI_MarginModelRight` | `'9'` |
| 是否规范用户才能激活 | `THOST_FTDC_SPI_IsStandardActive` | `'8'` |
| 上传的交易所结算文件路径 | `THOST_FTDC_SPI_UploadSettlementFile` | `'U'` |
| 上报保证金监控中心文件路径 | `THOST_FTDC_SPI_DownloadCSRCFile` | `'D'` |
| 生成的结算单文件路径 | `THOST_FTDC_SPI_SettlementBillFile` | `'S'` |
| 证监会文件标识 | `THOST_FTDC_SPI_CSRCOthersFile` | `'C'` |
| 投资者照片路径 | `THOST_FTDC_SPI_InvestorPhoto` | `'P'` |
| 全结经纪公司上传文件路径 | `THOST_FTDC_SPI_CSRCData` | `'R'` |
| 开户密码录入方式 | `THOST_FTDC_SPI_InvestorPwdModel` | `'I'` |
| 投资者中金所结算文件下载路径 | `THOST_FTDC_SPI_CFFEXInvestorSettleFile` | `'F'` |
| 投资者代码编码方式 | `THOST_FTDC_SPI_InvestorIDType` | `'a'` |
| 休眠户最高权益 | `THOST_FTDC_SPI_FreezeMaxReMain` | `'r'` |
| 手续费相关操作实时上场开关 | `THOST_FTDC_SPI_IsSync` | `'A'` |
| 解除开仓权限限制 | `THOST_FTDC_SPI_RelieveOpenLimit` | `'O'` |
| 是否规范用户才能休眠 | `THOST_FTDC_SPI_IsStandardFreeze` | `'X'` |
| 郑商所是否开放所有品种套保交易 | `THOST_FTDC_SPI_CZCENormalProductHedge` | `'B'` |

#### 52. TradeParamIDType

交易系统参数代码类型

`typedef char TThostFtdcTradeParamIDType;`

|名称|宏定义|常量|
|--|--|--|
| 系统加密算法 | `THOST_FTDC_TPID_EncryptionStandard` | `'E'` |
| 系统风险算法 | `THOST_FTDC_TPID_RiskMode` | `'R'` |
| 系统风险算法是否全局 0-否 1-是 | `THOST_FTDC_TPID_RiskModeGlobal` | `'G'` |
| 密码加密算法 | `THOST_FTDC_TPID_modeEncode` | `'P'` |
| 价格小数位数参数 | `THOST_FTDC_TPID_tickMode` | `'T'` |
| 用户最大会话数 | `THOST_FTDC_TPID_SingleUserSessionMaxNum` | `'S'` |
| 最大连续登录失败数 | `THOST_FTDC_TPID_LoginFailMaxNum` | `'L'` |
| 是否强制认证 | `THOST_FTDC_TPID_IsAuthForce` | `'A'` |
| 是否冻结证券持仓 | `THOST_FTDC_TPID_IsPosiFreeze` | `'F'` |
| 是否限仓 | `THOST_FTDC_TPID_IsPosiLimit` | `'M'` |
| 郑商所询价时间间隔 | `THOST_FTDC_TPID_ForQuoteTimeInterval` | `'Q'` |
| 是否期货限仓 | `THOST_FTDC_TPID_IsFuturePosiLimit` | `'B'` |
| 是否期货下单频率限制 | `THOST_FTDC_TPID_IsFutureOrderFreq` | `'C'` |
| 行权冻结是否计算盈利 | `THOST_FTDC_TPID_IsExecOrderProfit` | `'H'` |
| 银期开户是否验证开户银行卡号是否是预留银行账户 | `THOST_FTDC_TPID_IsCheckBankAcc` | `'I'` |
| 弱密码最后修改日期 | `THOST_FTDC_TPID_PasswordDeadLine` | `'J'` |
| 强密码校验 | `THOST_FTDC_TPID_IsStrongPassword` | `'K'` |
| 自有资金质押比 | `THOST_FTDC_TPID_BalanceMorgage` | `'a'` |
| 最小密码长度 | `THOST_FTDC_TPID_MinPwdLen` | `'O'` |
| IP当日最大登陆失败次数 | `THOST_FTDC_TPID_LoginFailMaxNumForIP` | `'U'` |
| 密码有效期 | `THOST_FTDC_TPID_PasswordPeriod` | `'V'` |
| 历史密码重复限制次数 | `THOST_FTDC_TPID_PwdHistoryCmp` | `'X'` |

#### 53. FileIDType

文件标识类型

`typedef char TThostFtdcFileIDType;`

|名称|宏定义|常量|
|--|--|--|
| 资金数据 | `THOST_FTDC_FI_SettlementFund` | `'F'` |
| 成交数据 | `THOST_FTDC_FI_Trade` | `'T'` |
| 投资者持仓数据 | `THOST_FTDC_FI_InvestorPosition` | `'P'` |
| 投资者分项资金数据 | `THOST_FTDC_FI_SubEntryFund` | `'O'` |
| 组合持仓数据 | `THOST_FTDC_FI_CZCECombinationPos` | `'C'` |
| 上报保证金监控中心数据 | `THOST_FTDC_FI_CSRCData` | `'R'` |
| 郑商所平仓了结数据 | `THOST_FTDC_FI_CZCEClose` | `'L'` |
| 郑商所非平仓了结数据 | `THOST_FTDC_FI_CZCENoClose` | `'N'` |
| 持仓明细数据 | `THOST_FTDC_FI_PositionDtl` | `'D'` |
| 期权执行文件 | `THOST_FTDC_FI_OptionStrike` | `'S'` |
| 结算价比对文件 | `THOST_FTDC_FI_SettlementPriceComparison` | `'M'` |
| 上期所非持仓变动明细 | `THOST_FTDC_FI_NonTradePosChange` | `'B'` |

#### 54. FileTypeType

文件上传类型类型

`typedef char TThostFtdcFileTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 结算 | `THOST_FTDC_FUT_Settlement` | `'0'` |
| 核对 | `THOST_FTDC_FUT_Check` | `'1'` |

#### 55. FileFormatType

文件格式类型

`typedef char TThostFtdcFileFormatType;`

|名称|宏定义|常量|
|--|--|--|
| 文本文件(.txt) | `THOST_FTDC_FFT_Txt` | `'0'` |
| 压缩文件(.zip) | `THOST_FTDC_FFT_Zip` | `'1'` |
| DBF文件(.dbf) | `THOST_FTDC_FFT_DBF` | `'2'` |

#### 56. FileUploadStatusType

文件状态类型

`typedef char TThostFtdcFileUploadStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 上传成功 | `THOST_FTDC_FUS_SucceedUpload` | `'1'` |
| 上传失败 | `THOST_FTDC_FUS_FailedUpload` | `'2'` |
| 导入成功 | `THOST_FTDC_FUS_SucceedLoad` | `'3'` |
| 导入部分成功 | `THOST_FTDC_FUS_PartSucceedLoad` | `'4'` |
| 导入失败 | `THOST_FTDC_FUS_FailedLoad` | `'5'` |

#### 57. TransferDirectionType

移仓方向类型

`typedef char TThostFtdcTransferDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 移出 | `THOST_FTDC_TD_Out` | `'0'` |
| 移入 | `THOST_FTDC_TD_In` | `'1'` |

#### 58. SpecialCreateRuleType

特殊的创建规则类型

`typedef char TThostFtdcSpecialCreateRuleType;`

|名称|宏定义|常量|
|--|--|--|
| 没有特殊创建规则 | `THOST_FTDC_SC_NoSpecialRule` | `'0'` |
| 不包含春节 | `THOST_FTDC_SC_NoSpringFestival` | `'1'` |

#### 59. BasisPriceTypeType

挂牌基准价类型类型

`typedef char TThostFtdcBasisPriceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 上一合约结算价 | `THOST_FTDC_IPT_LastSettlement` | `'1'` |
| 上一合约收盘价 | `THOST_FTDC_IPT_LaseClose` | `'2'` |

#### 60. ProductLifePhaseType

产品生命周期状态类型

`typedef char TThostFtdcProductLifePhaseType;`

|名称|宏定义|常量|
|--|--|--|
| 活跃 | `THOST_FTDC_PLP_Active` | `'1'` |
| 不活跃 | `THOST_FTDC_PLP_NonActive` | `'2'` |
| 注销 | `THOST_FTDC_PLP_Canceled` | `'3'` |

#### 61. DeliveryModeType

交割方式类型

`typedef char TThostFtdcDeliveryModeType;`

|名称|宏定义|常量|
|--|--|--|
| 现金交割 | `THOST_FTDC_DM_CashDeliv` | `'1'` |
| 实物交割 | `THOST_FTDC_DM_CommodityDeliv` | `'2'` |

#### 62. FundIOTypeType

出入金类型类型

`typedef char TThostFtdcFundIOTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 出入金 | `THOST_FTDC_FIOT_FundIO` | `'1'` |
| 银期转帐 | `THOST_FTDC_FIOT_Transfer` | `'2'` |
| 银期换汇 | `THOST_FTDC_FIOT_SwapCurrency` | `'3'` |

#### 63. FundTypeType

资金类型类型

`typedef char TThostFtdcFundTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行存款 | `THOST_FTDC_FT_Deposite` | `'1'` |
| 分项资金 | `THOST_FTDC_FT_ItemFund` | `'2'` |
| 公司调整 | `THOST_FTDC_FT_Company` | `'3'` |
| 资金内转 | `THOST_FTDC_FT_InnerTransfer` | `'4'` |

#### 64. FundDirectionType

出入金方向类型

`typedef char TThostFtdcFundDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 入金 | `THOST_FTDC_FD_In` | `'1'` |
| 出金 | `THOST_FTDC_FD_Out` | `'2'` |

#### 65. FundStatusType

资金状态类型

`typedef char TThostFtdcFundStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已录入 | `THOST_FTDC_FS_Record` | `'1'` |
| 已复核 | `THOST_FTDC_FS_Check` | `'2'` |
| 已冲销 | `THOST_FTDC_FS_Charge` | `'3'` |

#### 66. PublishStatusType

发布状态类型

`typedef char TThostFtdcPublishStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未发布 | `THOST_FTDC_PS_None` | `'1'` |
| 正在发布 | `THOST_FTDC_PS_Publishing` | `'2'` |
| 已发布 | `THOST_FTDC_PS_Published` | `'3'` |

#### 67. SystemStatusType

系统状态类型

`typedef char TThostFtdcSystemStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 不活跃 | `THOST_FTDC_ES_NonActive` | `'1'` |
| 启动 | `THOST_FTDC_ES_Startup` | `'2'` |
| 交易开始初始化 | `THOST_FTDC_ES_Initialize` | `'3'` |
| 交易完成初始化 | `THOST_FTDC_ES_Initialized` | `'4'` |
| 收市开始 | `THOST_FTDC_ES_Close` | `'5'` |
| 收市完成 | `THOST_FTDC_ES_Closed` | `'6'` |
| 结算 | `THOST_FTDC_ES_Settlement` | `'7'` |

#### 68. SettlementStatusType

结算状态类型

`typedef char TThostFtdcSettlementStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 初始 | `THOST_FTDC_STS_Initialize` | `'0'` |
| 结算中 | `THOST_FTDC_STS_Settlementing` | `'1'` |
| 已结算 | `THOST_FTDC_STS_Settlemented` | `'2'` |
| 结算完成 | `THOST_FTDC_STS_Finished` | `'3'` |

#### 69. InvestorTypeType

投资者类型类型

`typedef char TThostFtdcInvestorTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 自然人 | `THOST_FTDC_CT_Person` | `'0'` |
| 法人 | `THOST_FTDC_CT_Company` | `'1'` |
| 投资基金 | `THOST_FTDC_CT_Fund` | `'2'` |
| 特殊法人 | `THOST_FTDC_CT_SpecialOrgan` | `'3'` |
| 资管户 | `THOST_FTDC_CT_Asset` | `'4'` |

#### 70. BrokerTypeType

经纪公司类型类型

`typedef char TThostFtdcBrokerTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 交易会员 | `THOST_FTDC_BT_Trade` | `'0'` |
| 交易结算会员 | `THOST_FTDC_BT_TradeSettle` | `'1'` |

#### 71. RiskLevelType

风险等级类型

`typedef char TThostFtdcRiskLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 低风险客户 | `THOST_FTDC_FAS_Low` | `'1'` |
| 普通客户 | `THOST_FTDC_FAS_Normal` | `'2'` |
| 关注客户 | `THOST_FTDC_FAS_Focus` | `'3'` |
| 风险客户 | `THOST_FTDC_FAS_Risk` | `'4'` |

#### 72. FeeAcceptStyleType

手续费收取方式类型

`typedef char TThostFtdcFeeAcceptStyleType;`

|名称|宏定义|常量|
|--|--|--|
| 按交易收取 | `THOST_FTDC_FAS_ByTrade` | `'1'` |
| 按交割收取 | `THOST_FTDC_FAS_ByDeliv` | `'2'` |
| 不收 | `THOST_FTDC_FAS_None` | `'3'` |
| 按指定手续费收取 | `THOST_FTDC_FAS_FixFee` | `'4'` |

#### 73. PasswordTypeType

密码类型类型

`typedef char TThostFtdcPasswordTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 交易密码 | `THOST_FTDC_PWDT_Trade` | `'1'` |
| 资金密码 | `THOST_FTDC_PWDT_Account` | `'2'` |

#### 74. AlgorithmType

盈亏算法类型

`typedef char TThostFtdcAlgorithmType;`

|名称|宏定义|常量|
|--|--|--|
| 浮盈浮亏都计算 | `THOST_FTDC_AG_All` | `'1'` |
| 浮盈不计，浮亏计 | `THOST_FTDC_AG_OnlyLost` | `'2'` |
| 浮盈计，浮亏不计 | `THOST_FTDC_AG_OnlyGain` | `'3'` |
| 浮盈浮亏都不计算 | `THOST_FTDC_AG_None` | `'4'` |

#### 75. IncludeCloseProfitType

是否包含平仓盈利类型

`typedef char TThostFtdcIncludeCloseProfitType;`

|名称|宏定义|常量|
|--|--|--|
| 包含平仓盈利 | `THOST_FTDC_ICP_Include` | `'0'` |
| 不包含平仓盈利 | `THOST_FTDC_ICP_NotInclude` | `'2'` |

#### 76. AllWithoutTradeType

是否受可提比例限制类型

`typedef char TThostFtdcAllWithoutTradeType;`

|名称|宏定义|常量|
|--|--|--|
| 无仓无成交不受可提比例限制 | `THOST_FTDC_AWT_Enable` | `'0'` |
| 受可提比例限制 | `THOST_FTDC_AWT_Disable` | `'2'` |
| 无仓不受可提比例限制 | `THOST_FTDC_AWT_NoHoldEnable` | `'3'` |

#### 77. FuturePwdFlagType

资金密码核对标志类型

`typedef char TThostFtdcFuturePwdFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 不核对 | `THOST_FTDC_FPWD_UnCheck` | `'0'` |
| 核对 | `THOST_FTDC_FPWD_Check` | `'1'` |

#### 78. TransferTypeType

银期转账类型类型

`typedef char TThostFtdcTransferTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行转期货 | `THOST_FTDC_TT_BankToFuture` | `'0'` |
| 期货转银行 | `THOST_FTDC_TT_FutureToBank` | `'1'` |

#### 79. TransferValidFlagType

转账有效标志类型

`typedef char TThostFtdcTransferValidFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 无效或失败 | `THOST_FTDC_TVF_Invalid` | `'0'` |
| 有效 | `THOST_FTDC_TVF_Valid` | `'1'` |
| 冲正 | `THOST_FTDC_TVF_Reverse` | `'2'` |

#### 80. ReasonType

事由类型

`typedef char TThostFtdcReasonType;`

|名称|宏定义|常量|
|--|--|--|
| 错单 | `THOST_FTDC_RN_CD` | `'0'` |
| 资金在途 | `THOST_FTDC_RN_ZT` | `'1'` |
| 其它 | `THOST_FTDC_RN_QT` | `'2'` |

#### 81. SexType

性别类型

`typedef char TThostFtdcSexType;`

|名称|宏定义|常量|
|--|--|--|
| 未知 | `THOST_FTDC_SEX_None` | `'0'` |
| 男 | `THOST_FTDC_SEX_Man` | `'1'` |
| 女 | `THOST_FTDC_SEX_Woman` | `'2'` |

#### 82. UserTypeType

用户类型类型

`typedef char TThostFtdcUserTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 投资者 | `THOST_FTDC_UT_Investor` | `'0'` |
| 操作员 | `THOST_FTDC_UT_Operator` | `'1'` |
| 管理员 | `THOST_FTDC_UT_SuperUser` | `'2'` |

#### 83. RateTypeType

费率类型类型

`typedef char TThostFtdcRateTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 保证金率 | `THOST_FTDC_RATETYPE_MarginRate` | `'2'` |

#### 84. NoteTypeType

通知类型类型

`typedef char TThostFtdcNoteTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 交易结算单 | `THOST_FTDC_NOTETYPE_TradeSettleBill` | `'1'` |
| 交易结算月报 | `THOST_FTDC_NOTETYPE_TradeSettleMonth` | `'2'` |
| 追加保证金通知书 | `THOST_FTDC_NOTETYPE_CallMarginNotes` | `'3'` |
| 强行平仓通知书 | `THOST_FTDC_NOTETYPE_ForceCloseNotes` | `'4'` |
| 成交通知书 | `THOST_FTDC_NOTETYPE_TradeNotes` | `'5'` |
| 交割通知书 | `THOST_FTDC_NOTETYPE_DelivNotes` | `'6'` |

#### 85. SettlementStyleType

结算单方式类型

`typedef char TThostFtdcSettlementStyleType;`

|名称|宏定义|常量|
|--|--|--|
| 逐日盯市 | `THOST_FTDC_SBS_Day` | `'1'` |
| 逐笔对冲 | `THOST_FTDC_SBS_Volume` | `'2'` |

#### 86. SettlementBillTypeType

结算单类型类型

`typedef char TThostFtdcSettlementBillTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 日报 | `THOST_FTDC_ST_Day` | `'0'` |
| 月报 | `THOST_FTDC_ST_Month` | `'1'` |

#### 87. UserRightTypeType

客户权限类型类型

`typedef char TThostFtdcUserRightTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 登录 | `THOST_FTDC_URT_Logon` | `'1'` |
| 银期转帐 | `THOST_FTDC_URT_Transfer` | `'2'` |
| 邮寄结算单 | `THOST_FTDC_URT_EMail` | `'3'` |
| 传真结算单 | `THOST_FTDC_URT_Fax` | `'4'` |
| 条件单 | `THOST_FTDC_URT_ConditionOrder` | `'5'` |

#### 88. MarginPriceTypeType

保证金价格类型类型

`typedef char TThostFtdcMarginPriceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 昨结算价 | `THOST_FTDC_MPT_PreSettlementPrice` | `'1'` |
| 最新价 | `THOST_FTDC_MPT_SettlementPrice` | `'2'` |
| 成交均价 | `THOST_FTDC_MPT_AveragePrice` | `'3'` |
| 开仓价 | `THOST_FTDC_MPT_OpenPrice` | `'4'` |

#### 89. BillGenStatusType

结算单生成状态类型

`typedef char TThostFtdcBillGenStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未生成 | `THOST_FTDC_BGS_None` | `'0'` |
| 生成中 | `THOST_FTDC_BGS_NoGenerated` | `'1'` |
| 已生成 | `THOST_FTDC_BGS_Generated` | `'2'` |

#### 90. AlgoTypeType

算法类型类型

`typedef char TThostFtdcAlgoTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 持仓处理算法 | `THOST_FTDC_AT_HandlePositionAlgo` | `'1'` |
| 寻找保证金率算法 | `THOST_FTDC_AT_FindMarginRateAlgo` | `'2'` |

#### 91. HandlePositionAlgoIDType

持仓处理算法编号类型

`typedef char TThostFtdcHandlePositionAlgoIDType;`

|名称|宏定义|常量|
|--|--|--|
| 基本 | `THOST_FTDC_HPA_Base` | `'1'` |
| 大连商品交易所 | `THOST_FTDC_HPA_DCE` | `'2'` |
| 郑州商品交易所 | `THOST_FTDC_HPA_CZCE` | `'3'` |

#### 92. FindMarginRateAlgoIDType

寻找保证金率算法编号类型

`typedef char TThostFtdcFindMarginRateAlgoIDType;`

|名称|宏定义|常量|
|--|--|--|
| 基本 | `THOST_FTDC_FMRA_Base` | `'1'` |
| 大连商品交易所 | `THOST_FTDC_FMRA_DCE` | `'2'` |
| 郑州商品交易所 | `THOST_FTDC_FMRA_CZCE` | `'3'` |

#### 93. HandleTradingAccountAlgoIDType

资金处理算法编号类型

`typedef char TThostFtdcHandleTradingAccountAlgoIDType;`

|名称|宏定义|常量|
|--|--|--|
| 基本 | `THOST_FTDC_HTAA_Base` | `'1'` |
| 大连商品交易所 | `THOST_FTDC_HTAA_DCE` | `'2'` |
| 郑州商品交易所 | `THOST_FTDC_HTAA_CZCE` | `'3'` |

#### 94. PersonTypeType

联系人类型类型

`typedef char TThostFtdcPersonTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 指定下单人 | `THOST_FTDC_PST_Order` | `'1'` |
| 开户授权人 | `THOST_FTDC_PST_Open` | `'2'` |
| 资金调拨人 | `THOST_FTDC_PST_Fund` | `'3'` |
| 结算单确认人 | `THOST_FTDC_PST_Settlement` | `'4'` |
| 法人 | `THOST_FTDC_PST_Company` | `'5'` |
| 法人代表 | `THOST_FTDC_PST_Corporation` | `'6'` |
| 投资者联系人 | `THOST_FTDC_PST_LinkMan` | `'7'` |
| 分户管理资产负责人 | `THOST_FTDC_PST_Ledger` | `'8'` |
| 托（保）管人 | `THOST_FTDC_PST_Trustee` | `'9'` |
| 托（保）管机构法人代表 | `THOST_FTDC_PST_TrusteeCorporation` | `'A'` |
| 托（保）管机构开户授权人 | `THOST_FTDC_PST_TrusteeOpen` | `'B'` |
| 托（保）管机构联系人 | `THOST_FTDC_PST_TrusteeContact` | `'C'` |
| 境外自然人参考证件 | `THOST_FTDC_PST_ForeignerRefer` | `'D'` |
| 法人代表参考证件 | `THOST_FTDC_PST_CorporationRefer` | `'E'` |

#### 95. QueryInvestorRangeType

查询范围类型

`typedef char TThostFtdcQueryInvestorRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有 | `THOST_FTDC_QIR_All` | `'1'` |
| 查询分类 | `THOST_FTDC_QIR_Group` | `'2'` |
| 单一投资者 | `THOST_FTDC_QIR_Single` | `'3'` |

#### 96. InvestorRiskStatusType

投资者风险状态类型

`typedef char TThostFtdcInvestorRiskStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_IRS_Normal` | `'1'` |
| 警告 | `THOST_FTDC_IRS_Warn` | `'2'` |
| 追保 | `THOST_FTDC_IRS_Call` | `'3'` |
| 强平 | `THOST_FTDC_IRS_Force` | `'4'` |
| 异常 | `THOST_FTDC_IRS_Exception` | `'5'` |

#### 97. UserEventTypeType

用户事件类型类型

`typedef char TThostFtdcUserEventTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 登录 | `THOST_FTDC_UET_Login` | `'1'` |
| 登出 | `THOST_FTDC_UET_Logout` | `'2'` |
| CTP校验通过 | `THOST_FTDC_UET_Trading` | `'3'` |
| CTP校验失败 | `THOST_FTDC_UET_TradingError` | `'4'` |
| 修改密码 | `THOST_FTDC_UET_UpdatePassword` | `'5'` |
| 客户端认证 | `THOST_FTDC_UET_Authenticate` | `'6'` |
| 终端信息上报 | `THOST_FTDC_UET_SubmitSysInfo` | `'7'` |
| 转账 | `THOST_FTDC_UET_Transfer` | `'8'` |
| 其他 | `THOST_FTDC_UET_Other` | `'9'` |
| 修改资金密码 | `THOST_FTDC_UET_UpdateTradingAccountPassword` | `'a'` |

#### 98. CloseStyleType

平仓方式类型

`typedef char TThostFtdcCloseStyleType;`

|名称|宏定义|常量|
|--|--|--|
| 先开先平 | `THOST_FTDC_ICS_Close` | `'0'` |
| 先平今再平昨 | `THOST_FTDC_ICS_CloseToday` | `'1'` |

#### 99. StatModeType

统计方式类型

`typedef char TThostFtdcStatModeType;`

|名称|宏定义|常量|
|--|--|--|
| ---- | `THOST_FTDC_SM_Non` | `'0'` |
| 按合约统计 | `THOST_FTDC_SM_Instrument` | `'1'` |
| 按产品统计 | `THOST_FTDC_SM_Product` | `'2'` |
| 按投资者统计 | `THOST_FTDC_SM_Investor` | `'3'` |

#### 100. ParkedOrderStatusType

预埋单状态类型

`typedef char TThostFtdcParkedOrderStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未发送 | `THOST_FTDC_PAOS_NotSend` | `'1'` |
| 已发送 | `THOST_FTDC_PAOS_Send` | `'2'` |
| 已删除 | `THOST_FTDC_PAOS_Deleted` | `'3'` |

#### 101. VirDealStatusType

处理状态类型

`typedef char TThostFtdcVirDealStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正在处理 | `THOST_FTDC_VDS_Dealing` | `'1'` |
| 处理成功 | `THOST_FTDC_VDS_DeaclSucceed` | `'2'` |

#### 102. OrgSystemIDType

原有系统代码类型

`typedef char TThostFtdcOrgSystemIDType;`

|名称|宏定义|常量|
|--|--|--|
| 综合交易平台 | `THOST_FTDC_ORGS_Standard` | `'0'` |
| 易盛系统 | `THOST_FTDC_ORGS_ESunny` | `'1'` |
| 金仕达V6系统 | `THOST_FTDC_ORGS_KingStarV6` | `'2'` |

#### 103. VirTradeStatusType

交易状态类型

`typedef char TThostFtdcVirTradeStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常处理中 | `THOST_FTDC_VTS_NaturalDeal` | `'0'` |
| 成功结束 | `THOST_FTDC_VTS_SucceedEnd` | `'1'` |
| 失败结束 | `THOST_FTDC_VTS_FailedEND` | `'2'` |
| 异常中 | `THOST_FTDC_VTS_Exception` | `'3'` |
| 已人工异常处理 | `THOST_FTDC_VTS_ManualDeal` | `'4'` |
| 通讯异常 ，请人工处理 | `THOST_FTDC_VTS_MesException` | `'5'` |
| 系统出错，请人工处理 | `THOST_FTDC_VTS_SysException` | `'6'` |

#### 104. VirBankAccTypeType

银行帐户类型类型

`typedef char TThostFtdcVirBankAccTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 存折 | `THOST_FTDC_VBAT_BankBook` | `'1'` |
| 储蓄卡 | `THOST_FTDC_VBAT_BankCard` | `'2'` |
| 信用卡 | `THOST_FTDC_VBAT_CreditCard` | `'3'` |

#### 105. VirementStatusType

银行帐户类型类型

`typedef char TThostFtdcVirementStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_VMS_Natural` | `'0'` |
| 销户 | `THOST_FTDC_VMS_Canceled` | `'9'` |

#### 106. VirementAvailAbilityType

有效标志类型

`typedef char TThostFtdcVirementAvailAbilityType;`

|名称|宏定义|常量|
|--|--|--|
| 未确认 | `THOST_FTDC_VAA_NoAvailAbility` | `'0'` |
| 有效 | `THOST_FTDC_VAA_AvailAbility` | `'1'` |
| 冲正 | `THOST_FTDC_VAA_Repeal` | `'2'` |

#### 107. VirementTradeCodeType

交易代码类型

`typedef char TThostFtdcVirementTradeCodeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行发起银行资金转期货 | `THOST_FTDC_VTC_BankBankToFuture` | `'102001'` |
| 银行发起期货资金转银行 | `THOST_FTDC_VTC_BankFutureToBank` | `'102002'` |
| 期货发起银行资金转期货 | `THOST_FTDC_VTC_FutureBankToFuture` | `'202001'` |
| 期货发起期货资金转银行 | `THOST_FTDC_VTC_FutureFutureToBank` | `'202002'` |

#### 108. AMLGenStatusType

Aml生成方式类型

`typedef char TThostFtdcAMLGenStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 程序生成 | `THOST_FTDC_GEN_Program` | `'0'` |
| 人工生成 | `THOST_FTDC_GEN_HandWork` | `'1'` |

#### 109. CFMMCKeyKindType

动态密钥类别(保证金监管)类型

`typedef char TThostFtdcCFMMCKeyKindType;`

|名称|宏定义|常量|
|--|--|--|
| 主动请求更新 | `THOST_FTDC_CFMMCKK_REQUEST` | `'R'` |
| CFMMC自动更新 | `THOST_FTDC_CFMMCKK_AUTO` | `'A'` |
| CFMMC手动更新 | `THOST_FTDC_CFMMCKK_MANUAL` | `'M'` |

#### 110. CertificationTypeType

证件类型类型

`typedef char TThostFtdcCertificationTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 身份证 | `THOST_FTDC_CFT_IDCard` | `'0'` |
| 护照 | `THOST_FTDC_CFT_Passport` | `'1'` |
| 军官证 | `THOST_FTDC_CFT_OfficerIDCard` | `'2'` |
| 士兵证 | `THOST_FTDC_CFT_SoldierIDCard` | `'3'` |
| 回乡证 | `THOST_FTDC_CFT_HomeComingCard` | `'4'` |
| 营业执照号 | `THOST_FTDC_CFT_LicenseNo` | `'6'` |
| 组织机构代码证 | `THOST_FTDC_CFT_InstitutionCodeCard` | `'7'` |
| 临时营业执照号 | `THOST_FTDC_CFT_TempLicenseNo` | `'8'` |
| 民办非企业登记证书 | `THOST_FTDC_CFT_NoEnterpriseLicenseNo` | `'9'` |
| 其他证件 | `THOST_FTDC_CFT_OtherCard` | `'x'` |
| 主管部门批文 | `THOST_FTDC_CFT_SuperDepAgree` | `'a'` |

#### 111. FileBusinessCodeType

文件业务功能类型

`typedef char TThostFtdcFileBusinessCodeType;`

|名称|宏定义|常量|
|--|--|--|
| 其他 | `THOST_FTDC_FBC_Others` | `'0'` |
| 转账交易明细对账 | `THOST_FTDC_FBC_TransferDetails` | `'1'` |
| 客户账户状态对账 | `THOST_FTDC_FBC_CustAccStatus` | `'2'` |
| 账户类交易明细对账 | `THOST_FTDC_FBC_AccountTradeDetails` | `'3'` |
| 期货账户信息变更明细对账 | `THOST_FTDC_FBC_FutureAccountChangeInfoDetails` | `'4'` |
| 客户资金台账余额明细对账 | `THOST_FTDC_FBC_CustMoneyDetail` | `'5'` |
| 客户销户结息明细对账 | `THOST_FTDC_FBC_CustCancelAccountInfo` | `'6'` |
| 客户资金余额对账结果 | `THOST_FTDC_FBC_CustMoneyResult` | `'7'` |
| 其它对账异常结果文件 | `THOST_FTDC_FBC_OthersExceptionResult` | `'8'` |
| 客户结息净额明细 | `THOST_FTDC_FBC_CustInterestNetMoneyDetails` | `'9'` |
| 客户资金交收明细 | `THOST_FTDC_FBC_CustMoneySendAndReceiveDetails` | `'a'` |
| 法人存管银行资金交收汇总 | `THOST_FTDC_FBC_CorporationMoneyTotal` | `'b'` |
| 主体间资金交收汇总 | `THOST_FTDC_FBC_MainbodyMoneyTotal` | `'c'` |
| 总分平衡监管数据 | `THOST_FTDC_FBC_MainPartMonitorData` | `'d'` |
| 存管银行备付金余额 | `THOST_FTDC_FBC_PreparationMoney` | `'e'` |
| 协办存管银行资金监管数据 | `THOST_FTDC_FBC_BankMoneyMonitorData` | `'f'` |

#### 112. CashExchangeCodeType

汇钞标志类型

`typedef char TThostFtdcCashExchangeCodeType;`

|名称|宏定义|常量|
|--|--|--|
| 汇 | `THOST_FTDC_CEC_Exchange` | `'1'` |
| 钞 | `THOST_FTDC_CEC_Cash` | `'2'` |

#### 113. YesNoIndicatorType

是或否标识类型

`typedef char TThostFtdcYesNoIndicatorType;`

|名称|宏定义|常量|
|--|--|--|
| 是 | `THOST_FTDC_YNI_Yes` | `'0'` |
| 否 | `THOST_FTDC_YNI_No` | `'1'` |

#### 114. BanlanceTypeType

余额类型类型

`typedef char TThostFtdcBanlanceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 当前余额 | `THOST_FTDC_BLT_CurrentMoney` | `'0'` |
| 可用余额 | `THOST_FTDC_BLT_UsableMoney` | `'1'` |
| 可取余额 | `THOST_FTDC_BLT_FetchableMoney` | `'2'` |
| 冻结余额 | `THOST_FTDC_BLT_FreezeMoney` | `'3'` |

#### 115. GenderType

性别类型

`typedef char TThostFtdcGenderType;`

|名称|宏定义|常量|
|--|--|--|
| 未知状态 | `THOST_FTDC_GD_Unknown` | `'0'` |
| 男 | `THOST_FTDC_GD_Male` | `'1'` |
| 女 | `THOST_FTDC_GD_Female` | `'2'` |

#### 116. FeePayFlagType

费用支付标志类型

`typedef char TThostFtdcFeePayFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 由受益方支付费用 | `THOST_FTDC_FPF_BEN` | `'0'` |
| 由发送方支付费用 | `THOST_FTDC_FPF_OUR` | `'1'` |
| 由发送方支付发起的费用，受益方支付接受的费用 | `THOST_FTDC_FPF_SHA` | `'2'` |

#### 117. PassWordKeyTypeType

密钥类型类型

`typedef char TThostFtdcPassWordKeyTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 交换密钥 | `THOST_FTDC_PWKT_ExchangeKey` | `'0'` |
| 密码密钥 | `THOST_FTDC_PWKT_PassWordKey` | `'1'` |
| MAC密钥 | `THOST_FTDC_PWKT_MACKey` | `'2'` |
| 报文密钥 | `THOST_FTDC_PWKT_MessageKey` | `'3'` |

#### 118. FBTPassWordTypeType

密码类型类型

`typedef char TThostFtdcFBTPassWordTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 查询 | `THOST_FTDC_PWT_Query` | `'0'` |
| 取款 | `THOST_FTDC_PWT_Fetch` | `'1'` |
| 转帐 | `THOST_FTDC_PWT_Transfer` | `'2'` |
| 交易 | `THOST_FTDC_PWT_Trade` | `'3'` |

#### 119. FBTEncryModeType

加密方式类型

`typedef char TThostFtdcFBTEncryModeType;`

|名称|宏定义|常量|
|--|--|--|
| 不加密 | `THOST_FTDC_EM_NoEncry` | `'0'` |
| DES | `THOST_FTDC_EM_DES` | `'1'` |
| 3DES | `THOST_FTDC_EM_3DES` | `'2'` |

#### 120. BankRepealFlagType

银行冲正标志类型

`typedef char TThostFtdcBankRepealFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 银行无需自动冲正 | `THOST_FTDC_BRF_BankNotNeedRepeal` | `'0'` |
| 银行待自动冲正 | `THOST_FTDC_BRF_BankWaitingRepeal` | `'1'` |
| 银行已自动冲正 | `THOST_FTDC_BRF_BankBeenRepealed` | `'2'` |

#### 121. BrokerRepealFlagType

期商冲正标志类型

`typedef char TThostFtdcBrokerRepealFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 期商无需自动冲正 | `THOST_FTDC_BRORF_BrokerNotNeedRepeal` | `'0'` |
| 期商待自动冲正 | `THOST_FTDC_BRORF_BrokerWaitingRepeal` | `'1'` |
| 期商已自动冲正 | `THOST_FTDC_BRORF_BrokerBeenRepealed` | `'2'` |

#### 122. InstitutionTypeType

机构类别类型

`typedef char TThostFtdcInstitutionTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行 | `THOST_FTDC_TS_Bank` | `'0'` |
| 期商 | `THOST_FTDC_TS_Future` | `'1'` |
| 券商 | `THOST_FTDC_TS_Store` | `'2'` |

#### 123. LastFragmentType

最后分片标志类型

`typedef char TThostFtdcLastFragmentType;`

|名称|宏定义|常量|
|--|--|--|
| 是最后分片 | `THOST_FTDC_LF_Yes` | `'0'` |
| 不是最后分片 | `THOST_FTDC_LF_No` | `'1'` |

#### 124. BankAccStatusType

银行账户状态类型

`typedef char TThostFtdcBankAccStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_BAS_Normal` | `'0'` |
| 冻结 | `THOST_FTDC_BAS_Freeze` | `'1'` |
| 挂失 | `THOST_FTDC_BAS_ReportLoss` | `'2'` |

#### 125. MoneyAccountStatusType

资金账户状态类型

`typedef char TThostFtdcMoneyAccountStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_MAS_Normal` | `'0'` |
| 销户 | `THOST_FTDC_MAS_Cancel` | `'1'` |

#### 126. ManageStatusType

存管状态类型

`typedef char TThostFtdcManageStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 指定存管 | `THOST_FTDC_MSS_Point` | `'0'` |
| 预指定 | `THOST_FTDC_MSS_PrePoint` | `'1'` |
| 撤销指定 | `THOST_FTDC_MSS_CancelPoint` | `'2'` |

#### 127. SystemTypeType

应用系统类型类型

`typedef char TThostFtdcSystemTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银期转帐 | `THOST_FTDC_SYT_FutureBankTransfer` | `'0'` |
| 银证转帐 | `THOST_FTDC_SYT_StockBankTransfer` | `'1'` |
| 第三方存管 | `THOST_FTDC_SYT_TheThirdPartStore` | `'2'` |

#### 128. TxnEndFlagType

银期转帐划转结果标志类型

`typedef char TThostFtdcTxnEndFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 正常处理中 | `THOST_FTDC_TEF_NormalProcessing` | `'0'` |
| 成功结束 | `THOST_FTDC_TEF_Success` | `'1'` |
| 失败结束 | `THOST_FTDC_TEF_Failed` | `'2'` |
| 异常中 | `THOST_FTDC_TEF_Abnormal` | `'3'` |
| 已人工异常处理 | `THOST_FTDC_TEF_ManualProcessedForException` | `'4'` |
| 通讯异常 ，请人工处理 | `THOST_FTDC_TEF_CommuFailedNeedManualProcess` | `'5'` |
| 系统出错，请人工处理 | `THOST_FTDC_TEF_SysErrorNeedManualProcess` | `'6'` |

#### 129. ProcessStatusType

银期转帐服务处理状态类型

`typedef char TThostFtdcProcessStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未处理 | `THOST_FTDC_PSS_NotProcess` | `'0'` |
| 开始处理 | `THOST_FTDC_PSS_StartProcess` | `'1'` |
| 处理完成 | `THOST_FTDC_PSS_Finished` | `'2'` |

#### 130. CustTypeType

客户类型类型

`typedef char TThostFtdcCustTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 自然人 | `THOST_FTDC_CUSTT_Person` | `'0'` |
| 机构户 | `THOST_FTDC_CUSTT_Institution` | `'1'` |

#### 131. FBTTransferDirectionType

银期转帐方向类型

`typedef char TThostFtdcFBTTransferDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 入金，银行转期货 | `THOST_FTDC_FBTTD_FromBankToFuture` | `'1'` |
| 出金，期货转银行 | `THOST_FTDC_FBTTD_FromFutureToBank` | `'2'` |

#### 132. OpenOrDestroyType

开销户类别类型

`typedef char TThostFtdcOpenOrDestroyType;`

|名称|宏定义|常量|
|--|--|--|
| 开户 | `THOST_FTDC_OOD_Open` | `'1'` |
| 销户 | `THOST_FTDC_OOD_Destroy` | `'0'` |

#### 133. AvailabilityFlagType

有效标志类型

`typedef char TThostFtdcAvailabilityFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 未确认 | `THOST_FTDC_AVAF_Invalid` | `'0'` |
| 有效 | `THOST_FTDC_AVAF_Valid` | `'1'` |
| 冲正 | `THOST_FTDC_AVAF_Repeal` | `'2'` |

#### 134. OrganTypeType

机构类型类型

`typedef char TThostFtdcOrganTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行代理 | `THOST_FTDC_OT_Bank` | `'1'` |
| 交易前置 | `THOST_FTDC_OT_Future` | `'2'` |
| 银期转帐平台管理 | `THOST_FTDC_OT_PlateForm` | `'9'` |

#### 135. OrganLevelType

机构级别类型

`typedef char TThostFtdcOrganLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 银行总行或期商总部 | `THOST_FTDC_OL_HeadQuarters` | `'1'` |
| 银行分中心或期货公司营业部 | `THOST_FTDC_OL_Branch` | `'2'` |

#### 136. ProtocalIDType

协议类型类型

`typedef char TThostFtdcProtocalIDType;`

|名称|宏定义|常量|
|--|--|--|
| 期商协议 | `THOST_FTDC_PID_FutureProtocal` | `'0'` |
| 工行协议 | `THOST_FTDC_PID_ICBCProtocal` | `'1'` |
| 农行协议 | `THOST_FTDC_PID_ABCProtocal` | `'2'` |
| 中国银行协议 | `THOST_FTDC_PID_CBCProtocal` | `'3'` |
| 建行协议 | `THOST_FTDC_PID_CCBProtocal` | `'4'` |
| 交行协议 | `THOST_FTDC_PID_BOCOMProtocal` | `'5'` |
| 银期转帐平台协议 | `THOST_FTDC_PID_FBTPlateFormProtocal` | `'X'` |

#### 137. ConnectModeType

套接字连接方式类型

`typedef char TThostFtdcConnectModeType;`

|名称|宏定义|常量|
|--|--|--|
| 短连接 | `THOST_FTDC_CM_ShortConnect` | `'0'` |
| 长连接 | `THOST_FTDC_CM_LongConnect` | `'1'` |

#### 138. SyncModeType

套接字通信方式类型

`typedef char TThostFtdcSyncModeType;`

|名称|宏定义|常量|
|--|--|--|
| 异步 | `THOST_FTDC_SRM_ASync` | `'0'` |
| 同步 | `THOST_FTDC_SRM_Sync` | `'1'` |

#### 139. BankAccTypeType

银行帐号类型类型

`typedef char TThostFtdcBankAccTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行存折 | `THOST_FTDC_BAT_BankBook` | `'1'` |
| 储蓄卡 | `THOST_FTDC_BAT_SavingCard` | `'2'` |
| 信用卡 | `THOST_FTDC_BAT_CreditCard` | `'3'` |

#### 140. FutureAccTypeType

期货公司帐号类型类型

`typedef char TThostFtdcFutureAccTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行存折 | `THOST_FTDC_FAT_BankBook` | `'1'` |
| 储蓄卡 | `THOST_FTDC_FAT_SavingCard` | `'2'` |
| 信用卡 | `THOST_FTDC_FAT_CreditCard` | `'3'` |

#### 141. OrganStatusType

接入机构状态类型

`typedef char TThostFtdcOrganStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 启用 | `THOST_FTDC_OS_Ready` | `'0'` |
| 签到 | `THOST_FTDC_OS_CheckIn` | `'1'` |
| 签退 | `THOST_FTDC_OS_CheckOut` | `'2'` |
| 对帐文件到达 | `THOST_FTDC_OS_CheckFileArrived` | `'3'` |
| 对帐 | `THOST_FTDC_OS_CheckDetail` | `'4'` |
| 日终清理 | `THOST_FTDC_OS_DayEndClean` | `'5'` |
| 注销 | `THOST_FTDC_OS_Invalid` | `'9'` |

#### 142. CCBFeeModeType

建行收费模式类型

`typedef char TThostFtdcCCBFeeModeType;`

|名称|宏定义|常量|
|--|--|--|
| 按金额扣收 | `THOST_FTDC_CCBFM_ByAmount` | `'1'` |
| 按月扣收 | `THOST_FTDC_CCBFM_ByMonth` | `'2'` |

#### 143. CommApiTypeType

通讯API类型类型

`typedef char TThostFtdcCommApiTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 客户端 | `THOST_FTDC_CAPIT_Client` | `'1'` |
| 服务端 | `THOST_FTDC_CAPIT_Server` | `'2'` |
| 交易系统的UserApi | `THOST_FTDC_CAPIT_UserApi` | `'3'` |

#### 144. LinkStatusType

连接状态类型

`typedef char TThostFtdcLinkStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已经连接 | `THOST_FTDC_LS_Connected` | `'1'` |
| 没有连接 | `THOST_FTDC_LS_Disconnected` | `'2'` |

#### 145. PwdFlagType

密码核对标志类型

`typedef char TThostFtdcPwdFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 不核对 | `THOST_FTDC_BPWDF_NoCheck` | `'0'` |
| 明文核对 | `THOST_FTDC_BPWDF_BlankCheck` | `'1'` |
| 密文核对 | `THOST_FTDC_BPWDF_EncryptCheck` | `'2'` |

#### 146. SecuAccTypeType

期货帐号类型类型

`typedef char TThostFtdcSecuAccTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 资金帐号 | `THOST_FTDC_SAT_AccountID` | `'1'` |
| 资金卡号 | `THOST_FTDC_SAT_CardID` | `'2'` |
| 上海股东帐号 | `THOST_FTDC_SAT_SHStockholderID` | `'3'` |
| 深圳股东帐号 | `THOST_FTDC_SAT_SZStockholderID` | `'4'` |

#### 147. TransferStatusType

转账交易状态类型

`typedef char TThostFtdcTransferStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_TRFS_Normal` | `'0'` |
| 被冲正 | `THOST_FTDC_TRFS_Repealed` | `'1'` |

#### 148. SponsorTypeType

发起方类型

`typedef char TThostFtdcSponsorTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期商 | `THOST_FTDC_SPTYPE_Broker` | `'0'` |
| 银行 | `THOST_FTDC_SPTYPE_Bank` | `'1'` |

#### 149. ReqRspTypeType

请求响应类别类型

`typedef char TThostFtdcReqRspTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 请求 | `THOST_FTDC_REQRSP_Request` | `'0'` |
| 响应 | `THOST_FTDC_REQRSP_Response` | `'1'` |

#### 150. FBTUserEventTypeType

银期转帐用户事件类型类型

`typedef char TThostFtdcFBTUserEventTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 签到 | `THOST_FTDC_FBTUET_SignIn` | `'0'` |
| 银行转期货 | `THOST_FTDC_FBTUET_FromBankToFuture` | `'1'` |
| 期货转银行 | `THOST_FTDC_FBTUET_FromFutureToBank` | `'2'` |
| 开户 | `THOST_FTDC_FBTUET_OpenAccount` | `'3'` |
| 销户 | `THOST_FTDC_FBTUET_CancelAccount` | `'4'` |
| 变更银行账户 | `THOST_FTDC_FBTUET_ChangeAccount` | `'5'` |
| 冲正银行转期货 | `THOST_FTDC_FBTUET_RepealFromBankToFuture` | `'6'` |
| 冲正期货转银行 | `THOST_FTDC_FBTUET_RepealFromFutureToBank` | `'7'` |
| 查询银行账户 | `THOST_FTDC_FBTUET_QueryBankAccount` | `'8'` |
| 查询期货账户 | `THOST_FTDC_FBTUET_QueryFutureAccount` | `'9'` |
| 签退 | `THOST_FTDC_FBTUET_SignOut` | `'A'` |
| 密钥同步 | `THOST_FTDC_FBTUET_SyncKey` | `'B'` |
| 预约开户 | `THOST_FTDC_FBTUET_ReserveOpenAccount` | `'C'` |
| 撤销预约开户 | `THOST_FTDC_FBTUET_CancelReserveOpenAccount` | `'D'` |
| 预约开户确认 | `THOST_FTDC_FBTUET_ReserveOpenAccountConfirm` | `'E'` |
| 其他 | `THOST_FTDC_FBTUET_Other` | `'Z'` |

#### 151. DBOperationType

记录操作类型类型

`typedef char TThostFtdcDBOperationType;`

|名称|宏定义|常量|
|--|--|--|
| 插入 | `THOST_FTDC_DBOP_Insert` | `'0'` |
| 更新 | `THOST_FTDC_DBOP_Update` | `'1'` |
| 删除 | `THOST_FTDC_DBOP_Delete` | `'2'` |

#### 152. SyncFlagType

同步标记类型

`typedef char TThostFtdcSyncFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 已同步 | `THOST_FTDC_SYNF_Yes` | `'0'` |
| 未同步 | `THOST_FTDC_SYNF_No` | `'1'` |

#### 153. SyncTypeType

同步类型类型

`typedef char TThostFtdcSyncTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 一次同步 | `THOST_FTDC_SYNT_OneOffSync` | `'0'` |
| 定时同步 | `THOST_FTDC_SYNT_TimerSync` | `'1'` |
| 定时完全同步 | `THOST_FTDC_SYNT_TimerFullSync` | `'2'` |

#### 154. ExDirectionType

换汇方向类型

`typedef char TThostFtdcExDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 结汇 | `THOST_FTDC_FBEDIR_Settlement` | `'0'` |
| 售汇 | `THOST_FTDC_FBEDIR_Sale` | `'1'` |

#### 155. FBEResultFlagType

换汇成功标志类型

`typedef char TThostFtdcFBEResultFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 成功 | `THOST_FTDC_FBERES_Success` | `'0'` |
| 账户余额不足 | `THOST_FTDC_FBERES_InsufficientBalance` | `'1'` |
| 交易结果未知 | `THOST_FTDC_FBERES_UnknownTrading` | `'8'` |
| 失败 | `THOST_FTDC_FBERES_Fail` | `'x'` |

#### 156. FBEExchStatusType

换汇交易状态类型

`typedef char TThostFtdcFBEExchStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_FBEES_Normal` | `'0'` |
| 交易重发 | `THOST_FTDC_FBEES_ReExchange` | `'1'` |

#### 157. FBEFileFlagType

换汇文件标志类型

`typedef char TThostFtdcFBEFileFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 数据包 | `THOST_FTDC_FBEFG_DataPackage` | `'0'` |
| 文件 | `THOST_FTDC_FBEFG_File` | `'1'` |

#### 158. FBEAlreadyTradeType

换汇已交易标志类型

`typedef char TThostFtdcFBEAlreadyTradeType;`

|名称|宏定义|常量|
|--|--|--|
| 未交易 | `THOST_FTDC_FBEAT_NotTrade` | `'0'` |
| 已交易 | `THOST_FTDC_FBEAT_Trade` | `'1'` |

#### 159. FBEUserEventTypeType

银期换汇用户事件类型类型

`typedef char TThostFtdcFBEUserEventTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 签到 | `THOST_FTDC_FBEUET_SignIn` | `'0'` |
| 换汇 | `THOST_FTDC_FBEUET_Exchange` | `'1'` |
| 换汇重发 | `THOST_FTDC_FBEUET_ReExchange` | `'2'` |
| 银行账户查询 | `THOST_FTDC_FBEUET_QueryBankAccount` | `'3'` |
| 换汇明细查询 | `THOST_FTDC_FBEUET_QueryExchDetial` | `'4'` |
| 换汇汇总查询 | `THOST_FTDC_FBEUET_QueryExchSummary` | `'5'` |
| 换汇汇率查询 | `THOST_FTDC_FBEUET_QueryExchRate` | `'6'` |
| 对账文件通知 | `THOST_FTDC_FBEUET_CheckBankAccount` | `'7'` |
| 签退 | `THOST_FTDC_FBEUET_SignOut` | `'8'` |
| 其他 | `THOST_FTDC_FBEUET_Other` | `'Z'` |

#### 160. FBEReqFlagType

换汇发送标志类型

`typedef char TThostFtdcFBEReqFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 未处理 | `THOST_FTDC_FBERF_UnProcessed` | `'0'` |
| 等待发送 | `THOST_FTDC_FBERF_WaitSend` | `'1'` |
| 发送成功 | `THOST_FTDC_FBERF_SendSuccess` | `'2'` |
| 发送失败 | `THOST_FTDC_FBERF_SendFailed` | `'3'` |
| 等待重发 | `THOST_FTDC_FBERF_WaitReSend` | `'4'` |

#### 161. NotifyClassType

风险通知类型类型

`typedef char TThostFtdcNotifyClassType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_NC_NOERROR` | `'0'` |
| 警示 | `THOST_FTDC_NC_Warn` | `'1'` |
| 追保 | `THOST_FTDC_NC_Call` | `'2'` |
| 强平 | `THOST_FTDC_NC_Force` | `'3'` |
| 穿仓 | `THOST_FTDC_NC_CHUANCANG` | `'4'` |
| 异常 | `THOST_FTDC_NC_Exception` | `'5'` |

#### 162. ForceCloseTypeType

强平单类型类型

`typedef char TThostFtdcForceCloseTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 手工强平 | `THOST_FTDC_FCT_Manual` | `'0'` |
| 单一投资者辅助强平 | `THOST_FTDC_FCT_Single` | `'1'` |
| 批量投资者辅助强平 | `THOST_FTDC_FCT_Group` | `'2'` |

#### 163. RiskNotifyMethodType

风险通知途径类型

`typedef char TThostFtdcRiskNotifyMethodType;`

|名称|宏定义|常量|
|--|--|--|
| 系统通知 | `THOST_FTDC_RNM_System` | `'0'` |
| 短信通知 | `THOST_FTDC_RNM_SMS` | `'1'` |
| 邮件通知 | `THOST_FTDC_RNM_EMail` | `'2'` |
| 人工通知 | `THOST_FTDC_RNM_Manual` | `'3'` |

#### 164. RiskNotifyStatusType

风险通知状态类型

`typedef char TThostFtdcRiskNotifyStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未生成 | `THOST_FTDC_RNS_NotGen` | `'0'` |
| 已生成未发送 | `THOST_FTDC_RNS_Generated` | `'1'` |
| 发送失败 | `THOST_FTDC_RNS_SendError` | `'2'` |
| 已发送未接收 | `THOST_FTDC_RNS_SendOk` | `'3'` |
| 已接收未确认 | `THOST_FTDC_RNS_Received` | `'4'` |
| 已确认 | `THOST_FTDC_RNS_Confirmed` | `'5'` |

#### 165. RiskUserEventType

风控用户操作事件类型

`typedef char TThostFtdcRiskUserEventType;`

|名称|宏定义|常量|
|--|--|--|
| 导出数据 | `THOST_FTDC_RUE_ExportData` | `'0'` |

#### 166. ConditionalOrderSortTypeType

条件单索引条件类型

`typedef char TThostFtdcConditionalOrderSortTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 使用最新价升序 | `THOST_FTDC_COST_LastPriceAsc` | `'0'` |
| 使用最新价降序 | `THOST_FTDC_COST_LastPriceDesc` | `'1'` |
| 使用卖价升序 | `THOST_FTDC_COST_AskPriceAsc` | `'2'` |
| 使用卖价降序 | `THOST_FTDC_COST_AskPriceDesc` | `'3'` |
| 使用买价升序 | `THOST_FTDC_COST_BidPriceAsc` | `'4'` |
| 使用买价降序 | `THOST_FTDC_COST_BidPriceDesc` | `'5'` |

#### 167. SendTypeType

报送状态类型

`typedef char TThostFtdcSendTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 未发送 | `THOST_FTDC_UOAST_NoSend` | `'0'` |
| 已发送 | `THOST_FTDC_UOAST_Sended` | `'1'` |
| 已生成 | `THOST_FTDC_UOAST_Generated` | `'2'` |
| 报送失败 | `THOST_FTDC_UOAST_SendFail` | `'3'` |
| 接收成功 | `THOST_FTDC_UOAST_Success` | `'4'` |
| 接收失败 | `THOST_FTDC_UOAST_Fail` | `'5'` |
| 取消报送 | `THOST_FTDC_UOAST_Cancel` | `'6'` |

#### 168. ClientIDStatusType

交易编码状态类型

`typedef char TThostFtdcClientIDStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未申请 | `THOST_FTDC_UOACS_NoApply` | `'1'` |
| 已提交申请 | `THOST_FTDC_UOACS_Submited` | `'2'` |
| 已发送申请 | `THOST_FTDC_UOACS_Sended` | `'3'` |
| 完成 | `THOST_FTDC_UOACS_Success` | `'4'` |
| 拒绝 | `THOST_FTDC_UOACS_Refuse` | `'5'` |
| 已撤销编码 | `THOST_FTDC_UOACS_Cancel` | `'6'` |

#### 169. QuestionTypeType

特有信息类型类型

`typedef char TThostFtdcQuestionTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 单选 | `THOST_FTDC_QT_Radio` | `'1'` |
| 多选 | `THOST_FTDC_QT_Option` | `'2'` |
| 填空 | `THOST_FTDC_QT_Blank` | `'3'` |

#### 170. BusinessTypeType

业务类型类型

`typedef char TThostFtdcBusinessTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 请求 | `THOST_FTDC_BT_Request` | `'1'` |
| 应答 | `THOST_FTDC_BT_Response` | `'2'` |
| 通知 | `THOST_FTDC_BT_Notice` | `'3'` |

#### 171. CfmmcReturnCodeType

监控中心返回码类型

`typedef char TThostFtdcCfmmcReturnCodeType;`

|名称|宏定义|常量|
|--|--|--|
| 成功 | `THOST_FTDC_CRC_Success` | `'0'` |
| 该客户已经有流程在处理中 | `THOST_FTDC_CRC_Working` | `'1'` |
| 监控中客户资料检查失败 | `THOST_FTDC_CRC_InfoFail` | `'2'` |
| 监控中实名制检查失败 | `THOST_FTDC_CRC_IDCardFail` | `'3'` |
| 其他错误 | `THOST_FTDC_CRC_OtherFail` | `'4'` |

#### 172. ClientTypeType

客户类型类型

`typedef char TThostFtdcClientTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有 | `THOST_FTDC_CfMMCCT_All` | `'0'` |
| 个人 | `THOST_FTDC_CfMMCCT_Person` | `'1'` |
| 单位 | `THOST_FTDC_CfMMCCT_Company` | `'2'` |
| 其他 | `THOST_FTDC_CfMMCCT_Other` | `'3'` |
| 特殊法人 | `THOST_FTDC_CfMMCCT_SpecialOrgan` | `'4'` |
| 资管户 | `THOST_FTDC_CfMMCCT_Asset` | `'5'` |

#### 173. ExchangeIDTypeType

交易所编号类型

`typedef char TThostFtdcExchangeIDTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 上海期货交易所 | `THOST_FTDC_EIDT_SHFE` | `'S'` |
| 郑州商品交易所 | `THOST_FTDC_EIDT_CZCE` | `'Z'` |
| 大连商品交易所 | `THOST_FTDC_EIDT_DCE` | `'D'` |
| 中国金融期货交易所 | `THOST_FTDC_EIDT_CFFEX` | `'J'` |
| 上海国际能源交易中心股份有限公司 | `THOST_FTDC_EIDT_INE` | `'N'` |

#### 174. ExClientIDTypeType

交易编码类型类型

`typedef char TThostFtdcExClientIDTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 套保 | `THOST_FTDC_ECIDT_Hedge` | `'1'` |
| 套利 | `THOST_FTDC_ECIDT_Arbitrage` | `'2'` |
| 投机 | `THOST_FTDC_ECIDT_Speculation` | `'3'` |

#### 175. UpdateFlagType

更新状态类型

`typedef char TThostFtdcUpdateFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 未更新 | `THOST_FTDC_UF_NoUpdate` | `'0'` |
| 更新全部信息成功 | `THOST_FTDC_UF_Success` | `'1'` |
| 更新全部信息失败 | `THOST_FTDC_UF_Fail` | `'2'` |
| 更新交易编码成功 | `THOST_FTDC_UF_TCSuccess` | `'3'` |
| 更新交易编码失败 | `THOST_FTDC_UF_TCFail` | `'4'` |
| 已丢弃 | `THOST_FTDC_UF_Cancel` | `'5'` |

#### 176. ApplyOperateIDType

申请动作类型

`typedef char TThostFtdcApplyOperateIDType;`

|名称|宏定义|常量|
|--|--|--|
| 开户 | `THOST_FTDC_AOID_OpenInvestor` | `'1'` |
| 修改身份信息 | `THOST_FTDC_AOID_ModifyIDCard` | `'2'` |
| 修改一般信息 | `THOST_FTDC_AOID_ModifyNoIDCard` | `'3'` |
| 申请交易编码 | `THOST_FTDC_AOID_ApplyTradingCode` | `'4'` |
| 撤销交易编码 | `THOST_FTDC_AOID_CancelTradingCode` | `'5'` |
| 销户 | `THOST_FTDC_AOID_CancelInvestor` | `'6'` |
| 账户休眠 | `THOST_FTDC_AOID_FreezeAccount` | `'8'` |
| 激活休眠账户 | `THOST_FTDC_AOID_ActiveFreezeAccount` | `'9'` |

#### 177. ApplyStatusIDType

申请状态类型

`typedef char TThostFtdcApplyStatusIDType;`

|名称|宏定义|常量|
|--|--|--|
| 未补全 | `THOST_FTDC_ASID_NoComplete` | `'1'` |
| 已提交 | `THOST_FTDC_ASID_Submited` | `'2'` |
| 已审核 | `THOST_FTDC_ASID_Checked` | `'3'` |
| 已拒绝 | `THOST_FTDC_ASID_Refused` | `'4'` |
| 已删除 | `THOST_FTDC_ASID_Deleted` | `'5'` |

#### 178. SendMethodType

发送方式类型

`typedef char TThostFtdcSendMethodType;`

|名称|宏定义|常量|
|--|--|--|
| 文件发送 | `THOST_FTDC_UOASM_ByAPI` | `'1'` |
| 电子发送 | `THOST_FTDC_UOASM_ByFile` | `'2'` |

#### 179. EventModeType

操作方法类型

`typedef char TThostFtdcEventModeType;`

|名称|宏定义|常量|
|--|--|--|
| 增加 | `THOST_FTDC_EvM_ADD` | `'1'` |
| 修改 | `THOST_FTDC_EvM_UPDATE` | `'2'` |
| 删除 | `THOST_FTDC_EvM_DELETE` | `'3'` |
| 复核 | `THOST_FTDC_EvM_CHECK` | `'4'` |
| 复制 | `THOST_FTDC_EvM_COPY` | `'5'` |
| 注销 | `THOST_FTDC_EvM_CANCEL` | `'6'` |
| 冲销 | `THOST_FTDC_EvM_Reverse` | `'7'` |

#### 180. UOAAutoSendType

统一开户申请自动发送类型

`typedef char TThostFtdcUOAAutoSendType;`

|名称|宏定义|常量|
|--|--|--|
| 自动发送并接收 | `THOST_FTDC_UOAA_ASR` | `'1'` |
| 自动发送，不自动接收 | `THOST_FTDC_UOAA_ASNR` | `'2'` |
| 不自动发送，自动接收 | `THOST_FTDC_UOAA_NSAR` | `'3'` |
| 不自动发送，也不自动接收 | `THOST_FTDC_UOAA_NSR` | `'4'` |

#### 181. FlowIDType

流程ID类型

`typedef char TThostFtdcFlowIDType;`

|名称|宏定义|常量|
|--|--|--|
| 投资者对应投资者组设置 | `THOST_FTDC_EvM_InvestorGroupFlow` | `'1'` |
| 投资者手续费率设置 | `THOST_FTDC_EvM_InvestorRate` | `'2'` |
| 投资者手续费率模板关系设置 | `THOST_FTDC_EvM_InvestorCommRateModel` | `'3'` |

#### 182. CheckLevelType

复核级别类型

`typedef char TThostFtdcCheckLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 零级复核 | `THOST_FTDC_CL_Zero` | `'0'` |
| 一级复核 | `THOST_FTDC_CL_One` | `'1'` |
| 二级复核 | `THOST_FTDC_CL_Two` | `'2'` |

#### 183. CheckStatusType

复核级别类型

`typedef char TThostFtdcCheckStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未复核 | `THOST_FTDC_CHS_Init` | `'0'` |
| 复核中 | `THOST_FTDC_CHS_Checking` | `'1'` |
| 已复核 | `THOST_FTDC_CHS_Checked` | `'2'` |
| 拒绝 | `THOST_FTDC_CHS_Refuse` | `'3'` |
| 作废 | `THOST_FTDC_CHS_Cancel` | `'4'` |

#### 184. UsedStatusType

生效状态类型

`typedef char TThostFtdcUsedStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未生效 | `THOST_FTDC_CHU_Unused` | `'0'` |
| 已生效 | `THOST_FTDC_CHU_Used` | `'1'` |
| 生效失败 | `THOST_FTDC_CHU_Fail` | `'2'` |

#### 185. BankAcountOriginType

账户来源类型

`typedef char TThostFtdcBankAcountOriginType;`

|名称|宏定义|常量|
|--|--|--|
| 手工录入 | `THOST_FTDC_BAO_ByAccProperty` | `'0'` |
| 银期转账 | `THOST_FTDC_BAO_ByFBTransfer` | `'1'` |

#### 186. MonthBillTradeSumType

结算单月报成交汇总方式类型

`typedef char TThostFtdcMonthBillTradeSumType;`

|名称|宏定义|常量|
|--|--|--|
| 同日同合约 | `THOST_FTDC_MBTS_ByInstrument` | `'0'` |
| 同日同合约同价格 | `THOST_FTDC_MBTS_ByDayInsPrc` | `'1'` |
| 同合约 | `THOST_FTDC_MBTS_ByDayIns` | `'2'` |

#### 187. FBTTradeCodeEnumType

银期交易代码枚举类型

`typedef char TThostFtdcFBTTradeCodeEnumType;`

|名称|宏定义|常量|
|--|--|--|
| 银行发起银行转期货 | `THOST_FTDC_FTC_BankLaunchBankToBroker` | `'102001'` |
| 期货发起银行转期货 | `THOST_FTDC_FTC_BrokerLaunchBankToBroker` | `'202001'` |
| 银行发起期货转银行 | `THOST_FTDC_FTC_BankLaunchBrokerToBank` | `'102002'` |
| 期货发起期货转银行 | `THOST_FTDC_FTC_BrokerLaunchBrokerToBank` | `'202002'` |

#### 188. OTPTypeType

动态令牌类型类型

`typedef char TThostFtdcOTPTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 无动态令牌 | `THOST_FTDC_OTP_NONE` | `'0'` |
| 时间令牌 | `THOST_FTDC_OTP_TOTP` | `'1'` |

#### 189. OTPStatusType

动态令牌状态类型

`typedef char TThostFtdcOTPStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未使用 | `THOST_FTDC_OTPS_Unused` | `'0'` |
| 已使用 | `THOST_FTDC_OTPS_Used` | `'1'` |
| 注销 | `THOST_FTDC_OTPS_Disuse` | `'2'` |

#### 190. BrokerUserTypeType

经济公司用户类型类型

`typedef char TThostFtdcBrokerUserTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 投资者 | `THOST_FTDC_BUT_Investor` | `'1'` |
| 操作员 | `THOST_FTDC_BUT_BrokerUser` | `'2'` |

#### 191. FutureTypeType

期货类型类型

`typedef char TThostFtdcFutureTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 商品期货 | `THOST_FTDC_FUTT_Commodity` | `'1'` |
| 金融期货 | `THOST_FTDC_FUTT_Financial` | `'2'` |

#### 192. FundEventTypeType

资金管理操作类型类型

`typedef char TThostFtdcFundEventTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 转账限额 | `THOST_FTDC_FET_Restriction` | `'0'` |
| 当日转账限额 | `THOST_FTDC_FET_TodayRestriction` | `'1'` |
| 期商流水 | `THOST_FTDC_FET_Transfer` | `'2'` |
| 资金冻结 | `THOST_FTDC_FET_Credit` | `'3'` |
| 投资者可提资金比例 | `THOST_FTDC_FET_InvestorWithdrawAlm` | `'4'` |
| 单个银行帐户转账限额 | `THOST_FTDC_FET_BankRestriction` | `'5'` |
| 银期签约账户 | `THOST_FTDC_FET_Accountregister` | `'6'` |
| 交易所出入金 | `THOST_FTDC_FET_ExchangeFundIO` | `'7'` |
| 投资者出入金 | `THOST_FTDC_FET_InvestorFundIO` | `'8'` |

#### 193. AccountSourceTypeType

资金账户来源类型

`typedef char TThostFtdcAccountSourceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银期同步 | `THOST_FTDC_AST_FBTransfer` | `'0'` |
| 手工录入 | `THOST_FTDC_AST_ManualEntry` | `'1'` |

#### 194. CodeSourceTypeType

交易编码来源类型

`typedef char TThostFtdcCodeSourceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 统一开户(已规范) | `THOST_FTDC_CST_UnifyAccount` | `'0'` |
| 手工录入(未规范) | `THOST_FTDC_CST_ManualEntry` | `'1'` |

#### 195. UserRangeType

操作员范围类型

`typedef char TThostFtdcUserRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有 | `THOST_FTDC_UR_All` | `'0'` |
| 单一操作员 | `THOST_FTDC_UR_Single` | `'1'` |

#### 196. ByGroupType

交易统计表按客户统计方式类型

`typedef char TThostFtdcByGroupType;`

|名称|宏定义|常量|
|--|--|--|
| 按投资者统计 | `THOST_FTDC_BG_Investor` | `'2'` |
| 按类统计 | `THOST_FTDC_BG_Group` | `'1'` |

#### 197. TradeSumStatModeType

交易统计表按范围统计方式类型

`typedef char TThostFtdcTradeSumStatModeType;`

|名称|宏定义|常量|
|--|--|--|
| 按合约统计 | `THOST_FTDC_TSSM_Instrument` | `'1'` |
| 按产品统计 | `THOST_FTDC_TSSM_Product` | `'2'` |
| 按交易所统计 | `THOST_FTDC_TSSM_Exchange` | `'3'` |

#### 198. ExprSetModeType

日期表达式设置类型类型

`typedef char TThostFtdcExprSetModeType;`

|名称|宏定义|常量|
|--|--|--|
| 相对已有规则设置 | `THOST_FTDC_ESM_Relative` | `'1'` |
| 典型设置 | `THOST_FTDC_ESM_Typical` | `'2'` |

#### 199. RateInvestorRangeType

投资者范围类型

`typedef char TThostFtdcRateInvestorRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 公司标准 | `THOST_FTDC_RIR_All` | `'1'` |
| 模板 | `THOST_FTDC_RIR_Model` | `'2'` |
| 单一投资者 | `THOST_FTDC_RIR_Single` | `'3'` |

#### 200. SyncDataStatusType

主次用系统数据同步状态类型

`typedef char TThostFtdcSyncDataStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未同步 | `THOST_FTDC_SDS_Initialize` | `'0'` |
| 同步中 | `THOST_FTDC_SDS_Settlementing` | `'1'` |
| 已同步 | `THOST_FTDC_SDS_Settlemented` | `'2'` |

#### 201. TradeSourceType

成交来源类型

`typedef char TThostFtdcTradeSourceType;`

|名称|宏定义|常量|
|--|--|--|
| 来自交易所普通回报 | `THOST_FTDC_TSRC_NORMAL` | `'0'` |
| 来自查询 | `THOST_FTDC_TSRC_QUERY` | `'1'` |

#### 202. FlexStatModeType

产品合约统计方式类型

`typedef char TThostFtdcFlexStatModeType;`

|名称|宏定义|常量|
|--|--|--|
| 产品统计 | `THOST_FTDC_FSM_Product` | `'1'` |
| 交易所统计 | `THOST_FTDC_FSM_Exchange` | `'2'` |
| 统计所有 | `THOST_FTDC_FSM_All` | `'3'` |

#### 203. ByInvestorRangeType

投资者范围统计方式类型

`typedef char TThostFtdcByInvestorRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 属性统计 | `THOST_FTDC_BIR_Property` | `'1'` |
| 统计所有 | `THOST_FTDC_BIR_All` | `'2'` |

#### 204. PropertyInvestorRangeType

投资者范围类型

`typedef char TThostFtdcPropertyInvestorRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有 | `THOST_FTDC_PIR_All` | `'1'` |
| 投资者属性 | `THOST_FTDC_PIR_Property` | `'2'` |
| 单一投资者 | `THOST_FTDC_PIR_Single` | `'3'` |

#### 205. FileStatusType

文件状态类型

`typedef char TThostFtdcFileStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未生成 | `THOST_FTDC_FIS_NoCreate` | `'0'` |
| 已生成 | `THOST_FTDC_FIS_Created` | `'1'` |
| 生成失败 | `THOST_FTDC_FIS_Failed` | `'2'` |

#### 206. FileGenStyleType

文件生成方式类型

`typedef char TThostFtdcFileGenStyleType;`

|名称|宏定义|常量|
|--|--|--|
| 下发 | `THOST_FTDC_FGS_FileTransmit` | `'0'` |
| 生成 | `THOST_FTDC_FGS_FileGen` | `'1'` |

#### 207. SysOperModeType

系统日志操作方法类型

`typedef char TThostFtdcSysOperModeType;`

|名称|宏定义|常量|
|--|--|--|
| 增加 | `THOST_FTDC_SoM_Add` | `'1'` |
| 修改 | `THOST_FTDC_SoM_Update` | `'2'` |
| 删除 | `THOST_FTDC_SoM_Delete` | `'3'` |
| 复制 | `THOST_FTDC_SoM_Copy` | `'4'` |
| 激活 | `THOST_FTDC_SoM_AcTive` | `'5'` |
| 注销 | `THOST_FTDC_SoM_CanCel` | `'6'` |
| 重置 | `THOST_FTDC_SoM_ReSet` | `'7'` |

#### 208. SysOperTypeType

系统日志操作类型类型

`typedef char TThostFtdcSysOperTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 修改操作员密码 | `THOST_FTDC_SoT_UpdatePassword` | `'0'` |
| 操作员组织架构关系 | `THOST_FTDC_SoT_UserDepartment` | `'1'` |
| 角色管理 | `THOST_FTDC_SoT_RoleManager` | `'2'` |
| 角色功能设置 | `THOST_FTDC_SoT_RoleFunction` | `'3'` |
| 基础参数设置 | `THOST_FTDC_SoT_BaseParam` | `'4'` |
| 设置操作员 | `THOST_FTDC_SoT_SetUserID` | `'5'` |
| 用户角色设置 | `THOST_FTDC_SoT_SetUserRole` | `'6'` |
| 用户IP限制 | `THOST_FTDC_SoT_UserIpRestriction` | `'7'` |
| 组织架构管理 | `THOST_FTDC_SoT_DepartmentManager` | `'8'` |
| 组织架构向查询分类复制 | `THOST_FTDC_SoT_DepartmentCopy` | `'9'` |
| 交易编码管理 | `THOST_FTDC_SoT_Tradingcode` | `'A'` |
| 投资者状态维护 | `THOST_FTDC_SoT_InvestorStatus` | `'B'` |
| 投资者权限管理 | `THOST_FTDC_SoT_InvestorAuthority` | `'C'` |
| 属性设置 | `THOST_FTDC_SoT_PropertySet` | `'D'` |
| 重置投资者密码 | `THOST_FTDC_SoT_ReSetInvestorPasswd` | `'E'` |
| 投资者个性信息维护 | `THOST_FTDC_SoT_InvestorPersonalityInfo` | `'F'` |

#### 209. CSRCDataQueyTypeType

上报数据查询类型类型

`typedef char TThostFtdcCSRCDataQueyTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 查询当前交易日报送的数据 | `THOST_FTDC_CSRCQ_Current` | `'0'` |
| 查询历史报送的代理经纪公司的数据 | `THOST_FTDC_CSRCQ_History` | `'1'` |

#### 210. FreezeStatusType

休眠状态类型

`typedef char TThostFtdcFreezeStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 活跃 | `THOST_FTDC_FRS_Normal` | `'1'` |
| 休眠 | `THOST_FTDC_FRS_Freeze` | `'0'` |

#### 211. StandardStatusType

规范状态类型

`typedef char TThostFtdcStandardStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已规范 | `THOST_FTDC_STST_Standard` | `'0'` |
| 未规范 | `THOST_FTDC_STST_NonStandard` | `'1'` |

#### 212. RightParamTypeType

配置类型类型

`typedef char TThostFtdcRightParamTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 休眠户 | `THOST_FTDC_RPT_Freeze` | `'1'` |
| 激活休眠户 | `THOST_FTDC_RPT_FreezeActive` | `'2'` |
| 开仓权限限制 | `THOST_FTDC_RPT_OpenLimit` | `'3'` |
| 解除开仓权限限制 | `THOST_FTDC_RPT_RelieveOpenLimit` | `'4'` |

#### 213. DataStatusType

反洗钱审核表数据状态类型

`typedef char TThostFtdcDataStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_AMLDS_Normal` | `'0'` |
| 已删除 | `THOST_FTDC_AMLDS_Deleted` | `'1'` |

#### 214. AMLCheckStatusType

审核状态类型

`typedef char TThostFtdcAMLCheckStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未复核 | `THOST_FTDC_AMLCHS_Init` | `'0'` |
| 复核中 | `THOST_FTDC_AMLCHS_Checking` | `'1'` |
| 已复核 | `THOST_FTDC_AMLCHS_Checked` | `'2'` |
| 拒绝上报 | `THOST_FTDC_AMLCHS_RefuseReport` | `'3'` |

#### 215. AmlDateTypeType

日期类型类型

`typedef char TThostFtdcAmlDateTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 检查日期 | `THOST_FTDC_AMLDT_DrawDay` | `'0'` |
| 发生日期 | `THOST_FTDC_AMLDT_TouchDay` | `'1'` |

#### 216. AmlCheckLevelType

审核级别类型

`typedef char TThostFtdcAmlCheckLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 零级审核 | `THOST_FTDC_AMLCL_CheckLevel0` | `'0'` |
| 一级审核 | `THOST_FTDC_AMLCL_CheckLevel1` | `'1'` |
| 二级审核 | `THOST_FTDC_AMLCL_CheckLevel2` | `'2'` |
| 三级审核 | `THOST_FTDC_AMLCL_CheckLevel3` | `'3'` |

#### 217. ExportFileTypeType

导出文件类型类型

`typedef char TThostFtdcExportFileTypeType;`

|名称|宏定义|常量|
|--|--|--|
| CSV | `THOST_FTDC_EFT_CSV` | `'0'` |
| Excel | `THOST_FTDC_EFT_EXCEL` | `'1'` |
| DBF | `THOST_FTDC_EFT_DBF` | `'2'` |

#### 218. SettleManagerTypeType

结算配置类型类型

`typedef char TThostFtdcSettleManagerTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 结算前准备 | `THOST_FTDC_SMT_Before` | `'1'` |
| 结算 | `THOST_FTDC_SMT_Settlement` | `'2'` |
| 结算后核对 | `THOST_FTDC_SMT_After` | `'3'` |
| 结算后处理 | `THOST_FTDC_SMT_Settlemented` | `'4'` |

#### 219. SettleManagerLevelType

结算配置等级类型

`typedef char TThostFtdcSettleManagerLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 必要 | `THOST_FTDC_SML_Must` | `'1'` |
| 警告 | `THOST_FTDC_SML_Alarm` | `'2'` |
| 提示 | `THOST_FTDC_SML_Prompt` | `'3'` |
| 不检查 | `THOST_FTDC_SML_Ignore` | `'4'` |

#### 220. SettleManagerGroupType

模块分组类型

`typedef char TThostFtdcSettleManagerGroupType;`

|名称|宏定义|常量|
|--|--|--|
| 交易所核对 | `THOST_FTDC_SMG_Exhcange` | `'1'` |
| 内部核对 | `THOST_FTDC_SMG_ASP` | `'2'` |
| 上报数据核对 | `THOST_FTDC_SMG_CSRC` | `'3'` |

#### 221. LimitUseTypeType

保值额度使用类型类型

`typedef char TThostFtdcLimitUseTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 可重复使用 | `THOST_FTDC_LUT_Repeatable` | `'1'` |
| 不可重复使用 | `THOST_FTDC_LUT_Unrepeatable` | `'2'` |

#### 222. DataResourceType

数据来源类型

`typedef char TThostFtdcDataResourceType;`

|名称|宏定义|常量|
|--|--|--|
| 本系统 | `THOST_FTDC_DAR_Settle` | `'1'` |
| 交易所 | `THOST_FTDC_DAR_Exchange` | `'2'` |
| 报送数据 | `THOST_FTDC_DAR_CSRC` | `'3'` |

#### 223. MarginTypeType

保证金类型类型

`typedef char TThostFtdcMarginTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 交易所保证金率 | `THOST_FTDC_MGT_ExchMarginRate` | `'0'` |
| 投资者保证金率 | `THOST_FTDC_MGT_InstrMarginRate` | `'1'` |
| 投资者交易保证金率 | `THOST_FTDC_MGT_InstrMarginRateTrade` | `'2'` |

#### 224. ActiveTypeType

生效类型类型

`typedef char TThostFtdcActiveTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 仅当日生效 | `THOST_FTDC_ACT_Intraday` | `'1'` |
| 长期生效 | `THOST_FTDC_ACT_Long` | `'2'` |

#### 225. MarginRateTypeType

冲突保证金率类型类型

`typedef char TThostFtdcMarginRateTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 交易所保证金率 | `THOST_FTDC_MRT_Exchange` | `'1'` |
| 投资者保证金率 | `THOST_FTDC_MRT_Investor` | `'2'` |
| 投资者交易保证金率 | `THOST_FTDC_MRT_InvestorTrade` | `'3'` |

#### 226. BackUpStatusType

备份数据状态类型

`typedef char TThostFtdcBackUpStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未生成备份数据 | `THOST_FTDC_BUS_UnBak` | `'0'` |
| 备份数据生成中 | `THOST_FTDC_BUS_BakUp` | `'1'` |
| 已生成备份数据 | `THOST_FTDC_BUS_BakUped` | `'2'` |
| 备份数据失败 | `THOST_FTDC_BUS_BakFail` | `'3'` |

#### 227. InitSettlementType

结算初始化状态类型

`typedef char TThostFtdcInitSettlementType;`

|名称|宏定义|常量|
|--|--|--|
| 结算初始化未开始 | `THOST_FTDC_SIS_UnInitialize` | `'0'` |
| 结算初始化中 | `THOST_FTDC_SIS_Initialize` | `'1'` |
| 结算初始化完成 | `THOST_FTDC_SIS_Initialized` | `'2'` |

#### 228. ReportStatusType

报表数据生成状态类型

`typedef char TThostFtdcReportStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未生成报表数据 | `THOST_FTDC_SRS_NoCreate` | `'0'` |
| 报表数据生成中 | `THOST_FTDC_SRS_Create` | `'1'` |
| 已生成报表数据 | `THOST_FTDC_SRS_Created` | `'2'` |
| 生成报表数据失败 | `THOST_FTDC_SRS_CreateFail` | `'3'` |

#### 229. SaveStatusType

数据归档状态类型

`typedef char TThostFtdcSaveStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 归档未完成 | `THOST_FTDC_SSS_UnSaveData` | `'0'` |
| 归档完成 | `THOST_FTDC_SSS_SaveDatad` | `'1'` |

#### 230. SettArchiveStatusType

结算确认数据归档状态类型

`typedef char TThostFtdcSettArchiveStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 未归档数据 | `THOST_FTDC_SAS_UnArchived` | `'0'` |
| 数据归档中 | `THOST_FTDC_SAS_Archiving` | `'1'` |
| 已归档数据 | `THOST_FTDC_SAS_Archived` | `'2'` |
| 归档数据失败 | `THOST_FTDC_SAS_ArchiveFail` | `'3'` |

#### 231. CTPTypeType

CTP交易系统类型类型

`typedef char TThostFtdcCTPTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 未知类型 | `THOST_FTDC_CTPT_Unkown` | `'0'` |
| 主中心 | `THOST_FTDC_CTPT_MainCenter` | `'1'` |
| 备中心 | `THOST_FTDC_CTPT_BackUp` | `'2'` |

#### 232. CloseDealTypeType

平仓处理类型类型

`typedef char TThostFtdcCloseDealTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_CDT_Normal` | `'0'` |
| 投机平仓优先 | `THOST_FTDC_CDT_SpecFirst` | `'1'` |

#### 233. MortgageFundUseRangeType

货币质押资金可用范围类型

`typedef char TThostFtdcMortgageFundUseRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 不能使用 | `THOST_FTDC_MFUR_None` | `'0'` |
| 用于保证金 | `THOST_FTDC_MFUR_Margin` | `'1'` |
| 用于手续费、盈亏、保证金 | `THOST_FTDC_MFUR_All` | `'2'` |
| 人民币方案3 | `THOST_FTDC_MFUR_CNY3` | `'3'` |

#### 234. SpecProductTypeType

特殊产品类型类型

`typedef char TThostFtdcSpecProductTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 郑商所套保产品 | `THOST_FTDC_SPT_CzceHedge` | `'1'` |
| 货币质押产品 | `THOST_FTDC_SPT_IneForeignCurrency` | `'2'` |
| 大连短线开平仓产品 | `THOST_FTDC_SPT_DceOpenClose` | `'3'` |

#### 235. FundMortgageTypeType

货币质押类型类型

`typedef char TThostFtdcFundMortgageTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 质押 | `THOST_FTDC_FMT_Mortgage` | `'1'` |
| 解质 | `THOST_FTDC_FMT_Redemption` | `'2'` |

#### 236. AccountSettlementParamIDType

投资者账户结算参数代码类型

`typedef char TThostFtdcAccountSettlementParamIDType;`

|名称|宏定义|常量|
|--|--|--|
| 基础保证金 | `THOST_FTDC_ASPI_BaseMargin` | `'1'` |
| 最低权益标准 | `THOST_FTDC_ASPI_LowestInterest` | `'2'` |

#### 237. FundMortDirectionType

货币质押方向类型

`typedef char TThostFtdcFundMortDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 货币质入 | `THOST_FTDC_FMD_In` | `'1'` |
| 货币质出 | `THOST_FTDC_FMD_Out` | `'2'` |

#### 238. BusinessClassType

换汇类别类型

`typedef char TThostFtdcBusinessClassType;`

|名称|宏定义|常量|
|--|--|--|
| 盈利 | `THOST_FTDC_BT_Profit` | `'0'` |
| 亏损 | `THOST_FTDC_BT_Loss` | `'1'` |
| 其他 | `THOST_FTDC_BT_Other` | `'Z'` |

#### 239. SwapSourceTypeType

换汇数据来源类型

`typedef char TThostFtdcSwapSourceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 手工 | `THOST_FTDC_SST_Manual` | `'0'` |
| 自动生成 | `THOST_FTDC_SST_Automatic` | `'1'` |

#### 240. CurrExDirectionType

换汇类型类型

`typedef char TThostFtdcCurrExDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 结汇 | `THOST_FTDC_CED_Settlement` | `'0'` |
| 售汇 | `THOST_FTDC_CED_Sale` | `'1'` |

#### 241. CurrencySwapStatusType

申请状态类型

`typedef char TThostFtdcCurrencySwapStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已录入 | `THOST_FTDC_CSS_Entry` | `'1'` |
| 已审核 | `THOST_FTDC_CSS_Approve` | `'2'` |
| 已拒绝 | `THOST_FTDC_CSS_Refuse` | `'3'` |
| 已撤销 | `THOST_FTDC_CSS_Revoke` | `'4'` |
| 已发送 | `THOST_FTDC_CSS_Send` | `'5'` |
| 换汇成功 | `THOST_FTDC_CSS_Success` | `'6'` |
| 换汇失败 | `THOST_FTDC_CSS_Failure` | `'7'` |

#### 242. ReqFlagType

换汇发送标志类型

`typedef char TThostFtdcReqFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 未发送 | `THOST_FTDC_REQF_NoSend` | `'0'` |
| 发送成功 | `THOST_FTDC_REQF_SendSuccess` | `'1'` |
| 发送失败 | `THOST_FTDC_REQF_SendFailed` | `'2'` |
| 等待重发 | `THOST_FTDC_REQF_WaitReSend` | `'3'` |

#### 243. ResFlagType

换汇返回成功标志类型

`typedef char TThostFtdcResFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 成功 | `THOST_FTDC_RESF_Success` | `'0'` |
| 账户余额不足 | `THOST_FTDC_RESF_InsuffiCient` | `'1'` |
| 交易结果未知 | `THOST_FTDC_RESF_UnKnown` | `'8'` |

#### 244. ExStatusType

修改状态类型

`typedef char TThostFtdcExStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 修改前 | `THOST_FTDC_EXS_Before` | `'0'` |
| 修改后 | `THOST_FTDC_EXS_After` | `'1'` |

#### 245. ClientRegionType

开户客户地域类型

`typedef char TThostFtdcClientRegionType;`

|名称|宏定义|常量|
|--|--|--|
| 国内客户 | `THOST_FTDC_CR_Domestic` | `'1'` |
| 港澳台客户 | `THOST_FTDC_CR_GMT` | `'2'` |
| 国外客户 | `THOST_FTDC_CR_Foreign` | `'3'` |

#### 246. HasBoardType

是否有董事会类型

`typedef char TThostFtdcHasBoardType;`

|名称|宏定义|常量|
|--|--|--|
| 没有 | `THOST_FTDC_HB_No` | `'0'` |
| 有 | `THOST_FTDC_HB_Yes` | `'1'` |

#### 247. StartModeType

启动模式类型

`typedef char TThostFtdcStartModeType;`

|名称|宏定义|常量|
|--|--|--|
| 正常 | `THOST_FTDC_SM_Normal` | `'1'` |
| 应急 | `THOST_FTDC_SM_Emerge` | `'2'` |
| 恢复 | `THOST_FTDC_SM_Restore` | `'3'` |

#### 248. TemplateTypeType

模型类型类型

`typedef char TThostFtdcTemplateTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 全量 | `THOST_FTDC_TPT_Full` | `'1'` |
| 增量 | `THOST_FTDC_TPT_Increment` | `'2'` |
| 备份 | `THOST_FTDC_TPT_BackUp` | `'3'` |

#### 249. LoginModeType

登录模式类型

`typedef char TThostFtdcLoginModeType;`

|名称|宏定义|常量|
|--|--|--|
| 交易 | `THOST_FTDC_LM_Trade` | `'0'` |
| 转账 | `THOST_FTDC_LM_Transfer` | `'1'` |

#### 250. PromptTypeType

日历提示类型类型

`typedef char TThostFtdcPromptTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 合约上下市 | `THOST_FTDC_CPT_Instrument` | `'1'` |
| 保证金分段生效 | `THOST_FTDC_CPT_Margin` | `'2'` |

#### 251. HasTrusteeType

是否有托管人类型

`typedef char TThostFtdcHasTrusteeType;`

|名称|宏定义|常量|
|--|--|--|
| 有 | `THOST_FTDC_HT_Yes` | `'1'` |
| 没有 | `THOST_FTDC_HT_No` | `'0'` |

#### 252. AmTypeType

机构类型类型

`typedef char TThostFtdcAmTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 银行 | `THOST_FTDC_AMT_Bank` | `'1'` |
| 证券公司 | `THOST_FTDC_AMT_Securities` | `'2'` |
| 基金公司 | `THOST_FTDC_AMT_Fund` | `'3'` |
| 保险公司 | `THOST_FTDC_AMT_Insurance` | `'4'` |
| 信托公司 | `THOST_FTDC_AMT_Trust` | `'5'` |
| 其他 | `THOST_FTDC_AMT_Other` | `'9'` |

#### 253. CSRCFundIOTypeType

出入金类型类型

`typedef char TThostFtdcCSRCFundIOTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 出入金 | `THOST_FTDC_CFIOT_FundIO` | `'0'` |
| 银期换汇 | `THOST_FTDC_CFIOT_SwapCurrency` | `'1'` |

#### 254. CusAccountTypeType

结算账户类型类型

`typedef char TThostFtdcCusAccountTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期货结算账户 | `THOST_FTDC_CAT_Futures` | `'1'` |
| 纯期货资管业务下的资管结算账户 | `THOST_FTDC_CAT_AssetmgrFuture` | `'2'` |
| 综合类资管业务下的期货资管托管账户 | `THOST_FTDC_CAT_AssetmgrTrustee` | `'3'` |
| 综合类资管业务下的资金中转账户 | `THOST_FTDC_CAT_AssetmgrTransfer` | `'4'` |

#### 255. LanguageTypeType

通知语言类型类型

`typedef char TThostFtdcLanguageTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 中文 | `THOST_FTDC_LT_Chinese` | `'1'` |
| 英文 | `THOST_FTDC_LT_English` | `'2'` |

#### 256. AssetmgrClientTypeType

资产管理客户类型类型

`typedef char TThostFtdcAssetmgrClientTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 个人资管客户 | `THOST_FTDC_AMCT_Person` | `'1'` |
| 单位资管客户 | `THOST_FTDC_AMCT_Organ` | `'2'` |
| 特殊单位资管客户 | `THOST_FTDC_AMCT_SpecialOrgan` | `'4'` |

#### 257. AssetmgrTypeType

投资类型类型

`typedef char TThostFtdcAssetmgrTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期货类 | `THOST_FTDC_ASST_Futures` | `'3'` |
| 综合类 | `THOST_FTDC_ASST_SpecialOrgan` | `'4'` |

#### 258. CheckInstrTypeType

合约比较类型类型

`typedef char TThostFtdcCheckInstrTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 合约交易所不存在 | `THOST_FTDC_CIT_HasExch` | `'0'` |
| 合约本系统不存在 | `THOST_FTDC_CIT_HasATP` | `'1'` |
| 合约比较不一致 | `THOST_FTDC_CIT_HasDiff` | `'2'` |

#### 259. DeliveryTypeType

交割类型类型

`typedef char TThostFtdcDeliveryTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 手工交割 | `THOST_FTDC_DT_HandDeliv` | `'1'` |
| 到期交割 | `THOST_FTDC_DT_PersonDeliv` | `'2'` |

#### 260. MaxMarginSideAlgorithmType

大额单边保证金算法类型

`typedef char TThostFtdcMaxMarginSideAlgorithmType;`

|名称|宏定义|常量|
|--|--|--|
| 不使用大额单边保证金算法 | `THOST_FTDC_MMSA_NO` | `'0'` |
| 使用大额单边保证金算法 | `THOST_FTDC_MMSA_YES` | `'1'` |

#### 261. DAClientTypeType

资产管理客户类型类型

`typedef char TThostFtdcDAClientTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 自然人 | `THOST_FTDC_CACT_Person` | `'0'` |
| 法人 | `THOST_FTDC_CACT_Company` | `'1'` |
| 其他 | `THOST_FTDC_CACT_Other` | `'2'` |

#### 262. UOAAssetmgrTypeType

投资类型类型

`typedef char TThostFtdcUOAAssetmgrTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期货类 | `THOST_FTDC_UOAAT_Futures` | `'1'` |
| 综合类 | `THOST_FTDC_UOAAT_SpecialOrgan` | `'2'` |

#### 263. DirectionEnType

买卖方向类型

`typedef char TThostFtdcDirectionEnType;`

|名称|宏定义|常量|
|--|--|--|
| Buy | `THOST_FTDC_DEN_Buy` | `'0'` |
| Sell | `THOST_FTDC_DEN_Sell` | `'1'` |

#### 264. OffsetFlagEnType

开平标志类型

`typedef char TThostFtdcOffsetFlagEnType;`

|名称|宏定义|常量|
|--|--|--|
| Position Opening | `THOST_FTDC_OFEN_Open` | `'0'` |
| Position Close | `THOST_FTDC_OFEN_Close` | `'1'` |
| Forced Liquidation | `THOST_FTDC_OFEN_ForceClose` | `'2'` |
| Close Today | `THOST_FTDC_OFEN_CloseToday` | `'3'` |
| Close Prev. | `THOST_FTDC_OFEN_CloseYesterday` | `'4'` |
| Forced Reduction | `THOST_FTDC_OFEN_ForceOff` | `'5'` |
| Local Forced Liquidation | `THOST_FTDC_OFEN_LocalForceClose` | `'6'` |

#### 265. HedgeFlagEnType

投机套保标志类型

`typedef char TThostFtdcHedgeFlagEnType;`

|名称|宏定义|常量|
|--|--|--|
| Speculation | `THOST_FTDC_HFEN_Speculation` | `'1'` |
| Arbitrage | `THOST_FTDC_HFEN_Arbitrage` | `'2'` |
| Hedge | `THOST_FTDC_HFEN_Hedge` | `'3'` |

#### 266. FundIOTypeEnType

出入金类型类型

`typedef char TThostFtdcFundIOTypeEnType;`

|名称|宏定义|常量|
|--|--|--|
| Deposit | `THOST_FTDC_FIOTEN_FundIO` | `'1'` |
| Bank-Futures Transfer | `THOST_FTDC_FIOTEN_Transfer` | `'2'` |
| Bank-Futures FX Exchange | `THOST_FTDC_FIOTEN_SwapCurrency` | `'3'` |

#### 267. FundTypeEnType

资金类型类型

`typedef char TThostFtdcFundTypeEnType;`

|名称|宏定义|常量|
|--|--|--|
| Bank Deposit | `THOST_FTDC_FTEN_Deposite` | `'1'` |
| Payment | `THOST_FTDC_FTEN_ItemFund` | `'2'` |
| Brokerage Adj | `THOST_FTDC_FTEN_Company` | `'3'` |
| Internal Transfer | `THOST_FTDC_FTEN_InnerTransfer` | `'4'` |

#### 268. FundDirectionEnType

出入金方向类型

`typedef char TThostFtdcFundDirectionEnType;`

|名称|宏定义|常量|
|--|--|--|
| Deposit | `THOST_FTDC_FDEN_In` | `'1'` |
| Withdrawal | `THOST_FTDC_FDEN_Out` | `'2'` |

#### 269. FundMortDirectionEnType

货币质押方向类型

`typedef char TThostFtdcFundMortDirectionEnType;`

|名称|宏定义|常量|
|--|--|--|
| Pledge | `THOST_FTDC_FMDEN_In` | `'1'` |
| Redemption | `THOST_FTDC_FMDEN_Out` | `'2'` |

#### 270. OptionsTypeType

期权类型类型

`typedef char TThostFtdcOptionsTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 看涨 | `THOST_FTDC_CP_CallOptions` | `'1'` |
| 看跌 | `THOST_FTDC_CP_PutOptions` | `'2'` |

#### 271. StrikeModeType

执行方式类型

`typedef char TThostFtdcStrikeModeType;`

|名称|宏定义|常量|
|--|--|--|
| 欧式 | `THOST_FTDC_STM_Continental` | `'0'` |
| 美式 | `THOST_FTDC_STM_American` | `'1'` |
| 百慕大 | `THOST_FTDC_STM_Bermuda` | `'2'` |

#### 272. StrikeTypeType

执行类型类型

`typedef char TThostFtdcStrikeTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 自身对冲 | `THOST_FTDC_STT_Hedge` | `'0'` |
| 匹配执行 | `THOST_FTDC_STT_Match` | `'1'` |

#### 273. ApplyTypeType

中金所期权放弃执行申请类型类型

`typedef char TThostFtdcApplyTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 不执行数量 | `THOST_FTDC_APPT_NotStrikeNum` | `'4'` |

#### 274. GiveUpDataSourceType

放弃执行申请数据来源类型

`typedef char TThostFtdcGiveUpDataSourceType;`

|名称|宏定义|常量|
|--|--|--|
| 系统生成 | `THOST_FTDC_GUDS_Gen` | `'0'` |
| 手工添加 | `THOST_FTDC_GUDS_Hand` | `'1'` |

#### 275. ExecResultType

执行结果类型

`typedef char TThostFtdcExecResultType;`

|名称|宏定义|常量|
|--|--|--|
| 没有执行 | `THOST_FTDC_OER_NoExec` | `'n'` |
| 已经取消 | `THOST_FTDC_OER_Canceled` | `'c'` |
| 执行成功 | `THOST_FTDC_OER_OK` | `'0'` |
| 期权持仓不够 | `THOST_FTDC_OER_NoPosition` | `'1'` |
| 资金不够 | `THOST_FTDC_OER_NoDeposit` | `'2'` |
| 会员不存在 | `THOST_FTDC_OER_NoParticipant` | `'3'` |
| 客户不存在 | `THOST_FTDC_OER_NoClient` | `'4'` |
| 合约不存在 | `THOST_FTDC_OER_NoInstrument` | `'6'` |
| 没有执行权限 | `THOST_FTDC_OER_NoRight` | `'7'` |
| 不合理的数量 | `THOST_FTDC_OER_InvalidVolume` | `'8'` |
| 没有足够的历史成交 | `THOST_FTDC_OER_NoEnoughHistoryTrade` | `'9'` |
| 未知 | `THOST_FTDC_OER_Unknown` | `'a'` |

#### 276. CombinationTypeType

组合类型类型

`typedef char TThostFtdcCombinationTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期货组合 | `THOST_FTDC_COMBT_Future` | `'0'` |
| 垂直价差BUL | `THOST_FTDC_COMBT_BUL` | `'1'` |
| 垂直价差BER | `THOST_FTDC_COMBT_BER` | `'2'` |
| 跨式组合 | `THOST_FTDC_COMBT_STD` | `'3'` |
| 宽跨式组合 | `THOST_FTDC_COMBT_STG` | `'4'` |
| 备兑组合 | `THOST_FTDC_COMBT_PRT` | `'5'` |
| 时间价差组合 | `THOST_FTDC_COMBT_CAS` | `'6'` |
| 期权对锁组合 | `THOST_FTDC_COMBT_OPL` | `'7'` |
| 买备兑组合 | `THOST_FTDC_COMBT_BFO` | `'8'` |
| 买入期权垂直价差组合 | `THOST_FTDC_COMBT_BLS` | `'9'` |
| 卖出期权垂直价差组合 | `THOST_FTDC_COMBT_BES` | `'a'` |

#### 277. DceCombinationTypeType

组合类型类型

`typedef char TThostFtdcDceCombinationTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期货对锁组合 | `THOST_FTDC_DCECOMBT_SPL` | `'0'` |
| 期权对锁组合 | `THOST_FTDC_DCECOMBT_OPL` | `'1'` |
| 期货跨期组合 | `THOST_FTDC_DCECOMBT_SP` | `'2'` |
| 期货跨品种组合 | `THOST_FTDC_DCECOMBT_SPC` | `'3'` |
| 买入期权垂直价差组合 | `THOST_FTDC_DCECOMBT_BLS` | `'4'` |
| 卖出期权垂直价差组合 | `THOST_FTDC_DCECOMBT_BES` | `'5'` |
| 期权日历价差组合 | `THOST_FTDC_DCECOMBT_CAS` | `'6'` |
| 期权跨式组合 | `THOST_FTDC_DCECOMBT_STD` | `'7'` |
| 期权宽跨式组合 | `THOST_FTDC_DCECOMBT_STG` | `'8'` |
| 买入期货期权组合 | `THOST_FTDC_DCECOMBT_BFO` | `'9'` |
| 卖出期货期权组合 | `THOST_FTDC_DCECOMBT_SFO` | `'a'` |

#### 278. OptionRoyaltyPriceTypeType

期权权利金价格类型类型

`typedef char TThostFtdcOptionRoyaltyPriceTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 昨结算价 | `THOST_FTDC_ORPT_PreSettlementPrice` | `'1'` |
| 开仓价 | `THOST_FTDC_ORPT_OpenPrice` | `'4'` |
| 最新价与昨结算价较大值 | `THOST_FTDC_ORPT_MaxPreSettlementPrice` | `'5'` |

#### 279. BalanceAlgorithmType

权益算法类型

`typedef char TThostFtdcBalanceAlgorithmType;`

|名称|宏定义|常量|
|--|--|--|
| 不计算期权市值盈亏 | `THOST_FTDC_BLAG_Default` | `'1'` |
| 计算期权市值亏损 | `THOST_FTDC_BLAG_IncludeOptValLost` | `'2'` |

#### 280. ActionTypeType

执行类型类型

`typedef char TThostFtdcActionTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 执行 | `THOST_FTDC_ACTP_Exec` | `'1'` |
| 放弃 | `THOST_FTDC_ACTP_Abandon` | `'2'` |

#### 281. ForQuoteStatusType

询价状态类型

`typedef char TThostFtdcForQuoteStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 已经提交 | `THOST_FTDC_FQST_Submitted` | `'a'` |
| 已经接受 | `THOST_FTDC_FQST_Accepted` | `'b'` |
| 已经被拒绝 | `THOST_FTDC_FQST_Rejected` | `'c'` |

#### 282. ValueMethodType

取值方式类型

`typedef char TThostFtdcValueMethodType;`

|名称|宏定义|常量|
|--|--|--|
| 按绝对值 | `THOST_FTDC_VM_Absolute` | `'0'` |
| 按比率 | `THOST_FTDC_VM_Ratio` | `'1'` |

#### 283. ExecOrderPositionFlagType

期权行权后是否保留期货头寸的标记类型

`typedef char TThostFtdcExecOrderPositionFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 保留 | `THOST_FTDC_EOPF_Reserve` | `'0'` |
| 不保留 | `THOST_FTDC_EOPF_UnReserve` | `'1'` |

#### 284. ExecOrderCloseFlagType

期权行权后生成的头寸是否自动平仓类型

`typedef char TThostFtdcExecOrderCloseFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 自动平仓 | `THOST_FTDC_EOCF_AutoClose` | `'0'` |
| 免于自动平仓 | `THOST_FTDC_EOCF_NotToClose` | `'1'` |

#### 285. ProductTypeType

产品类型类型

`typedef char TThostFtdcProductTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期货 | `THOST_FTDC_PTE_Futures` | `'1'` |
| 期权 | `THOST_FTDC_PTE_Options` | `'2'` |

#### 286. CZCEUploadFileNameType

郑商所结算文件名类型

`typedef char TThostFtdcCZCEUploadFileNameType;`

|名称|宏定义|常量|
|--|--|--|
| ^\d{8}_zz_\d{4} | `THOST_FTDC_CUFN_CUFN_O` | `'O'` |
| ^\d{8}成交表 | `THOST_FTDC_CUFN_CUFN_T` | `'T'` |
| ^\d{8}单腿持仓表new | `THOST_FTDC_CUFN_CUFN_P` | `'P'` |
| ^\d{8}非平仓了结表 | `THOST_FTDC_CUFN_CUFN_N` | `'N'` |
| ^\d{8}平仓表 | `THOST_FTDC_CUFN_CUFN_L` | `'L'` |
| ^\d{8}资金表 | `THOST_FTDC_CUFN_CUFN_F` | `'F'` |
| ^\d{8}组合持仓表 | `THOST_FTDC_CUFN_CUFN_C` | `'C'` |
| ^\d{8}保证金参数表 | `THOST_FTDC_CUFN_CUFN_M` | `'M'` |

#### 287. DCEUploadFileNameType

大商所结算文件名类型

`typedef char TThostFtdcDCEUploadFileNameType;`

|名称|宏定义|常量|
|--|--|--|
| ^\d{8}_dl_\d{3} | `THOST_FTDC_DUFN_DUFN_O` | `'O'` |
| ^\d{8}_成交表 | `THOST_FTDC_DUFN_DUFN_T` | `'T'` |
| ^\d{8}_持仓表 | `THOST_FTDC_DUFN_DUFN_P` | `'P'` |
| ^\d{8}_资金结算表 | `THOST_FTDC_DUFN_DUFN_F` | `'F'` |
| ^\d{8}_优惠组合持仓明细表 | `THOST_FTDC_DUFN_DUFN_C` | `'C'` |
| ^\d{8}_持仓明细表 | `THOST_FTDC_DUFN_DUFN_D` | `'D'` |
| ^\d{8}_保证金参数表 | `THOST_FTDC_DUFN_DUFN_M` | `'M'` |
| ^\d{8}_期权执行表 | `THOST_FTDC_DUFN_DUFN_S` | `'S'` |

#### 288. SHFEUploadFileNameType

上期所结算文件名类型

`typedef char TThostFtdcSHFEUploadFileNameType;`

|名称|宏定义|常量|
|--|--|--|
| ^\d{4}_\d{8}_\d{8}_DailyFundChg | `THOST_FTDC_SUFN_SUFN_O` | `'O'` |
| ^\d{4}_\d{8}_\d{8}_Trade | `THOST_FTDC_SUFN_SUFN_T` | `'T'` |
| ^\d{4}_\d{8}_\d{8}_SettlementDetail | `THOST_FTDC_SUFN_SUFN_P` | `'P'` |
| ^\d{4}_\d{8}_\d{8}_Capital | `THOST_FTDC_SUFN_SUFN_F` | `'F'` |

#### 289. CFFEXUploadFileNameType

中金所结算文件名类型

`typedef char TThostFtdcCFFEXUploadFileNameType;`

|名称|宏定义|常量|
|--|--|--|
| ^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade | `THOST_FTDC_CFUFN_SUFN_T` | `'T'` |
| ^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail | `THOST_FTDC_CFUFN_SUFN_P` | `'P'` |
| ^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital | `THOST_FTDC_CFUFN_SUFN_F` | `'F'` |
| ^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec | `THOST_FTDC_CFUFN_SUFN_S` | `'S'` |

#### 290. CombDirectionType

组合指令方向类型

`typedef char TThostFtdcCombDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 申请组合 | `THOST_FTDC_CMDR_Comb` | `'0'` |
| 申请拆分 | `THOST_FTDC_CMDR_UnComb` | `'1'` |
| 操作员删组合单 | `THOST_FTDC_CMDR_DelComb` | `'2'` |

#### 291. StrikeOffsetTypeType

行权偏移类型类型

`typedef char TThostFtdcStrikeOffsetTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 实值额 | `THOST_FTDC_STOV_RealValue` | `'1'` |
| 盈利额 | `THOST_FTDC_STOV_ProfitValue` | `'2'` |
| 实值比例 | `THOST_FTDC_STOV_RealRatio` | `'3'` |
| 盈利比例 | `THOST_FTDC_STOV_ProfitRatio` | `'4'` |

#### 292. ReserveOpenAccStasType

预约开户状态类型

`typedef char TThostFtdcReserveOpenAccStasType;`

|名称|宏定义|常量|
|--|--|--|
| 等待处理中 | `THOST_FTDC_ROAST_Processing` | `'0'` |
| 已撤销 | `THOST_FTDC_ROAST_Cancelled` | `'1'` |
| 已开户 | `THOST_FTDC_ROAST_Opened` | `'2'` |
| 无效请求 | `THOST_FTDC_ROAST_Invalid` | `'3'` |

#### 293. WeakPasswordSourceType

弱密码来源类型

`typedef char TThostFtdcWeakPasswordSourceType;`

|名称|宏定义|常量|
|--|--|--|
| 弱密码库 | `THOST_FTDC_WPSR_Lib` | `'1'` |
| 手工录入 | `THOST_FTDC_WPSR_Manual` | `'2'` |

#### 294. OptSelfCloseFlagType

期权行权的头寸是否自对冲类型

`typedef char TThostFtdcOptSelfCloseFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 自对冲期权仓位 | `THOST_FTDC_OSCF_CloseSelfOptionPosition` | `'1'` |
| 保留期权仓位 | `THOST_FTDC_OSCF_ReserveOptionPosition` | `'2'` |
| 自对冲卖方履约后的期货仓位 | `THOST_FTDC_OSCF_SellCloseSelfFuturePosition` | `'3'` |
| 保留卖方履约后的期货仓位 | `THOST_FTDC_OSCF_ReserveFuturePosition` | `'4'` |

#### 295. BizTypeType

业务类型类型

`typedef char TThostFtdcBizTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 期货 | `THOST_FTDC_BZTP_Future` | `'1'` |
| 证券 | `THOST_FTDC_BZTP_Stock` | `'2'` |

#### 296. AppTypeType

用户App类型类型

`typedef char TThostFtdcAppTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 直连的投资者 | `THOST_FTDC_APP_TYPE_Investor` | `'1'` |
| 为每个投资者都创建连接的中继 | `THOST_FTDC_APP_TYPE_InvestorRelay` | `'2'` |
| 所有投资者共享一个操作员连接的中继 | `THOST_FTDC_APP_TYPE_OperatorRelay` | `'3'` |
| 未知 | `THOST_FTDC_APP_TYPE_UnKnown` | `'4'` |

#### 297. ResponseValueType

应答类型类型

`typedef char TThostFtdcResponseValueType;`

|名称|宏定义|常量|
|--|--|--|
| 检查成功 | `THOST_FTDC_RV_Right` | `'0'` |
| 检查失败 | `THOST_FTDC_RV_Refuse` | `'1'` |

#### 298. OTCTradeTypeType

OTC成交类型类型

`typedef char TThostFtdcOTCTradeTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 大宗交易 | `THOST_FTDC_OTC_TRDT_Block` | `'0'` |
| 期转现 | `THOST_FTDC_OTC_TRDT_EFP` | `'1'` |

#### 299. MatchTypeType

期现风险匹配方式类型

`typedef char TThostFtdcMatchTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 基点价值 | `THOST_FTDC_OTC_MT_DV01` | `'1'` |
| 面值 | `THOST_FTDC_OTC_MT_ParValue` | `'2'` |

#### 300. AuthTypeType

用户终端认证方式类型

`typedef char TThostFtdcAuthTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 白名单校验 | `THOST_FTDC_AU_WHITE` | `'0'` |
| 黑名单校验 | `THOST_FTDC_AU_BLACK` | `'1'` |

#### 301. ClassTypeType

合约分类方式类型

`typedef char TThostFtdcClassTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有合约 | `THOST_FTDC_INS_ALL` | `'0'` |
| 期货、即期、期转现、Tas、金属指数合约 | `THOST_FTDC_INS_FUTURE` | `'1'` |
| 期货、现货期权合约 | `THOST_FTDC_INS_OPTION` | `'2'` |
| 组合合约 | `THOST_FTDC_INS_COMB` | `'3'` |

#### 302. TradingTypeType

合约交易状态分类方式类型

`typedef char TThostFtdcTradingTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 所有状态 | `THOST_FTDC_TD_ALL` | `'0'` |
| 交易 | `THOST_FTDC_TD_TRADE` | `'1'` |
| 非交易 | `THOST_FTDC_TD_UNTRADE` | `'2'` |

#### 303. ProductStatusType

产品状态类型

`typedef char TThostFtdcProductStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 可交易 | `THOST_FTDC_PS_tradeable` | `'1'` |
| 不可交易 | `THOST_FTDC_PS_untradeable` | `'2'` |

#### 304. SyncDeltaStatusType

追平状态类型

`typedef char TThostFtdcSyncDeltaStatusType;`

|名称|宏定义|常量|
|--|--|--|
| 交易可读 | `THOST_FTDC_SDS_Readable` | `'1'` |
| 交易在读 | `THOST_FTDC_SDS_Reading` | `'2'` |
| 交易读取完成 | `THOST_FTDC_SDS_Readend` | `'3'` |
| 追平失败 交易本地状态结算不存在 | `THOST_FTDC_SDS_OptErr` | `'e'` |

#### 305. ActionDirectionType

操作标志类型

`typedef char TThostFtdcActionDirectionType;`

|名称|宏定义|常量|
|--|--|--|
| 增加 | `THOST_FTDC_ACD_Add` | `'1'` |
| 删除 | `THOST_FTDC_ACD_Del` | `'2'` |
| 更新 | `THOST_FTDC_ACD_Upd` | `'3'` |

#### 306. OrderCancelAlgType

撤单时选择席位算法类型

`typedef char TThostFtdcOrderCancelAlgType;`

|名称|宏定义|常量|
|--|--|--|
| 轮询席位撤单 | `THOST_FTDC_OAC_Balance` | `'1'` |
| 优先原报单席位撤单 | `THOST_FTDC_OAC_OrigFirst` | `'2'` |

#### 307. OpenLimitControlLevelType

开仓量限制粒度类型

`typedef char TThostFtdcOpenLimitControlLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 不控制 | `THOST_FTDC_PLCL_None` | `'0'` |
| 产品级别 | `THOST_FTDC_PLCL_Product` | `'1'` |
| 合约级别 | `THOST_FTDC_PLCL_Inst` | `'2'` |

#### 308. OrderFreqControlLevelType

报单频率控制粒度类型

`typedef char TThostFtdcOrderFreqControlLevelType;`

|名称|宏定义|常量|
|--|--|--|
| 不控制 | `THOST_FTDC_OFCL_None` | `'0'` |
| 产品级别 | `THOST_FTDC_OFCL_Product` | `'1'` |
| 合约级别 | `THOST_FTDC_OFCL_Inst` | `'2'` |

#### 309. EnumBoolType

枚举bool类型类型

`typedef char TThostFtdcEnumBoolType;`

|名称|宏定义|常量|
|--|--|--|
| false | `THOST_FTDC_EBL_False` | `'0'` |
| true | `THOST_FTDC_EBL_True` | `'1'` |

#### 310. TimeRangeType

期货合约阶段标识类型

`typedef char TThostFtdcTimeRangeType;`

|名称|宏定义|常量|
|--|--|--|
| 一般月份 | `THOST_FTDC_ETR_USUAL` | `'1'` |
| 交割月前一个月上半月 | `THOST_FTDC_ETR_FNSP` | `'2'` |
| 交割月前一个月下半月 | `THOST_FTDC_ETR_BNSP` | `'3'` |
| 交割月份 | `THOST_FTDC_ETR_SPOT` | `'4'` |

#### 311. PortfolioType

新型组保算法类型

`typedef char TThostFtdcPortfolioType;`

|名称|宏定义|常量|
|--|--|--|
| 不使用新型组保算法 | `THOST_FTDC_EPF_None` | `'0'` |
| SPBM算法 | `THOST_FTDC_EPF_SPBM` | `'1'` |
| RULE算法 | `THOST_FTDC_EPF_RULE` | `'2'` |
| SPMM算法 | `THOST_FTDC_EPF_SPMM` | `'3'` |
| RCAMS算法 | `THOST_FTDC_EPF_RCAMS` | `'4'` |

#### 312. WithDrawParamIDType

可提参数代码类型

`typedef char TThostFtdcWithDrawParamIDType;`

|名称|宏定义|常量|
|--|--|--|
| 权利金收支是否可提 1 代表可提 0 不可提 | `THOST_FTDC_WDPID_CashIn` | `'C'` |

#### 313. InvstTradingRightType

投资者交易权限类型

`typedef char TThostFtdcInvstTradingRightType;`

|名称|宏定义|常量|
|--|--|--|
| 只能平仓 | `THOST_FTDC_ITR_CloseOnly` | `'1'` |
| 不能交易 | `THOST_FTDC_ITR_Forbidden` | `'2'` |

#### 314. InstMarginCalIDType

SPMM合约保证金算法类型

`typedef char TThostFtdcInstMarginCalIDType;`

|名称|宏定义|常量|
|--|--|--|
| 标准算法收取双边 | `THOST_FTDC_IMID_BothSide` | `'1'` |
| 单向大边 | `THOST_FTDC_IMID_MMSA` | `'2'` |
| 新组保SPMM | `THOST_FTDC_IMID_SPMM` | `'3'` |

#### 315. RCAMSCombinationTypeType

RCAMS组合类型类型

`typedef char TThostFtdcRCAMSCombinationTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 牛市看涨价差组合 | `THOST_FTDC_ERComb_BUC` | `'0'` |
| 熊市看涨价差组合 | `THOST_FTDC_ERComb_BEC` | `'1'` |
| 熊市看跌价差组合 | `THOST_FTDC_ERComb_BEP` | `'2'` |
| 牛市看跌价差组合 | `THOST_FTDC_ERComb_BUP` | `'3'` |
| 日历价差组合 | `THOST_FTDC_ERComb_CAS` | `'4'` |

#### 316. PortfTypeType

新组保算法启用类型类型

`typedef char TThostFtdcPortfTypeType;`

|名称|宏定义|常量|
|--|--|--|
| 使用初版交易所算法 | `THOST_FTDC_EET_None` | `'0'` |
| SPBM算法V1.1.0_附加保证金调整 | `THOST_FTDC_EET_SPBM_AddOnHedge` | `'1'` |

#### 317. InstrumentClassType

合约类型类型

`typedef char TThostFtdcInstrumentClassType;`

|名称|宏定义|常量|
|--|--|--|
| 一般月份合约 | `THOST_FTDC_EIC_Usual` | `'1'` |
| 临近交割合约 | `THOST_FTDC_EIC_Delivery` | `'2'` |
| 非组合合约 | `THOST_FTDC_EIC_NonComb` | `'3'` |

#### 318. ProdChangeFlagType

品种记录改变状态类型

`typedef char TThostFtdcProdChangeFlagType;`

|名称|宏定义|常量|
|--|--|--|
| 持仓量和冻结量均无变化 | `THOST_FTDC_PCF_None` | `'0'` |
| 持仓量无变化，冻结量有变化 | `THOST_FTDC_PCF_OnlyFrozen` | `'1'` |
| 持仓量有变化 | `THOST_FTDC_PCF_PositionChange` | `'2'` |

#### 319. PwdRcdSrcType

历史密码来源类型

`typedef char TThostFtdcPwdRcdSrcType;`

|名称|宏定义|常量|
|--|--|--|
| 来源于Sync初始化数据 | `THOST_FTDC_PRS_Init` | `'0'` |
| 来源于实时上场数据 | `THOST_FTDC_PRS_Sync` | `'1'` |
| 来源于用户修改 | `THOST_FTDC_PRS_UserUpd` | `'2'` |
| 来源于超户修改，很可能来自主席同步数据 | `THOST_FTDC_PRS_SuperUserUpd` | `'3'` |

