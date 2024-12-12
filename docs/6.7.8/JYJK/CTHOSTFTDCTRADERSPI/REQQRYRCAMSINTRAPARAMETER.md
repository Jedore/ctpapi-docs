<p>请求RCAMS品种内风险对冲参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTRAPARAMETER/">OnRspQryRCAMSIntraParameter</a></p>
<span class="anchor" id="9bc8d0a2-2016-43e6-b04e-220afdbad9d4"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSIntraParameter(CThostFtdcQryRCAMSIntraParameterField *pQryRCAMSIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="19b8ab38-5840-4d70-8813-0d458ce5b281"></span>
## 2.参数
<p>pQryRCAMSIntraParameter：RCAMS品种内风险对冲参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">产品组合代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="59d30dd0-73f0-4144-a25b-66cc8cbb7c05"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2dcbe63c-bcb2-48db-a4db-00b8c59802d3"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="fe59017e-d075-43b9-8dd4-0287ff129147"></span>
## 5.FAQ
<p>无</p>
